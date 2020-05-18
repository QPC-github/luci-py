# Copyright 2020 The LUCI Authors. All rights reserved.
# Use of this source code is governed under the Apache License, Version 2.0
# that can be found in the LICENSE file.

import logging

from components import auth

from proto.config import realms_pb2
from server import config
from server import pools_config
from server import task_scheduler


def get_permission_name(enum_permission):
  """ Generates Realm permission name from enum value.

  e.g. realms_pb2.REALM_PERMISSION_POOLS_CREATE_TASK
       -> 'swarming.pools.createTask'

  Args:
    enum_permission: realms_pb2.RealmPermission enum value.

  Returns:
    realm_permission: Realm permission name 'swarming.<subject>.<verb>'
  """
  enum_name = realms_pb2.RealmPermission.Name(enum_permission)
  words = enum_name.replace('REALM_PERMISSION_', '').split('_')
  # convert first word to subject e.g. pools, tasks
  subject = words[0].lower()
  # convert following words to verb e.g. createTask, listBots
  verb = words[1].lower() + ''.join(map(lambda x: x.capitalize(), words[2:]))
  return 'swarming.%s.%s' % (subject, verb)


def is_enforced_permission(perm, pool_cfg=None):
  """ Checks if the Realm permission is enforced.

  Checks if the permission is specified in `enforced_realm_permissions`
  in settings.cfg or pools.cfg for the pool.

  Args:
    perm: realms_pb2.RealmPermission enum value.
    pool_cfg: PoolConfig of the pool

  Returns:
    bool: True if it's enforced, False if it's legacy-compatible.
  """
  if pool_cfg and perm in pool_cfg.enforced_realm_permissions:
    return True
  return perm in config.settings().auth.enforced_realm_permissions


def check_pools_create_task(task_request):
  """Checks if the caller can create the task in the pool.

  Realm permission `swarming.pools.createTask` will be checked,
  using auth.has_permission() or auth.has_permission_dryrun().

  If the realm permission check is enforced,
    It just calls auth.has_permission()

  If it's legacy-compatible,
    It calls the legacy task_scheduler.check_schedule_request_acl_caller() and
    compare the legacy result with the realm permission check using the dryrun.

  Args:
    task_request: TaskRequest entity to be scheduled.

  Returns:
    None

  Raises:
    auth.AuthorizationError: if the caller is not allowed to schedule the task
                             in the pool.
  """
  pool = task_request.pool
  pool_cfg = pools_config.get_pool_config(pool)

  if not pool_cfg:
    logging.warning('Pool "%s" is not in pools.cfg', pool)
    # Unknown pools are forbidden.
    raise auth.AuthorizationError('Pool "%s" not defined in pools.cfg' % pool)

  # 'swarming.pools.createTask'
  perm = get_permission_name(realms_pb2.REALM_PERMISSION_POOLS_CREATE_TASK)

  if is_enforced_permission(realms_pb2.REALM_PERMISSION_POOLS_CREATE_TASK,
                            pool_cfg):
    # enforced path.

    # pool.realm is required.
    if not pool_cfg.realm:
      raise auth.AuthorizationError('realm is missing in Pool "%s"' % pool)

    # check only Realm ACLs.
    if not auth.has_permission(perm, [pool_cfg.realm]):
      raise auth.AuthorizationError(
          'User "%s" is not allowed to schedule tasks in the pool "%s", '
          'see pools.cfg' % (auth.get_current_identity().to_bytes(), pool))
    return

  # legacy-compatible path

  # pool.realm is optional.
  if not pool_cfg.realm:
    logging.warning('crbug.com/1066839: realm is missing in Pool "%s"', pool)

  legacy_allowed = True
  try:
    task_scheduler.check_schedule_request_acl_caller(pool, pool_cfg)
  except auth.AuthorizationError:
    legacy_allowed = False
    raise  # re-raise the exception
  finally:
    # compare the legacy check result with realm check result if the pool realm
    # is specified.
    if pool_cfg.realm:
      auth.has_permission_dryrun(
          perm, [pool_cfg.realm],
          legacy_allowed,
          tracking_bug='crbug.com/1066839')


# TODO(crbug.com/1066839): implement and replace the legacy check function
# with check_tasks_run_as and check_pools_create_task.
def check_tasks_run_as(_task_request):
  """Checks if the task service account is allowed to run in the pool.

  Realm permission `swarming.tasks.runAs` will be checked,
  using auth.has_permission() or auth.has_permission_dryrun().

  If the realm permission check is enforced,
    It just calls auth.has_permission()

  If it's legacy-compatible,
    It calls task_scheduler.check_schedule_request_acl_service_account()
    and compare the legacy result with the realm permission check using
    the dryrun.

  Args:
    task_request: TaskRequest entity to be scheduled.

  Returns:
    None

  Raises:
    auth.AuthorizationError: if the service account is not allowed to run
                             in the pool.
  """
  pass