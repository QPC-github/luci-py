# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='config.proto',
  package='auth_service',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0c\x63onfig.proto\x12\x0c\x61uth_service\"D\n\x0bSettingsCfg\x12\x1c\n\x14\x65nable_ts_monitoring\x18\x01 \x01(\x08\x12\x17\n\x0f\x61uth_db_gs_path\x18\x02 \x01(\t\"\x93\x04\n\x13GroupImporterConfig\x12?\n\x07tarball\x18\x01 \x03(\x0b\x32..auth_service.GroupImporterConfig.TarballEntry\x12\x43\n\tplainlist\x18\x02 \x03(\x0b\x32\x30.auth_service.GroupImporterConfig.PlainlistEntry\x12L\n\x0etarball_upload\x18\x03 \x03(\x0b\x32\x34.auth_service.GroupImporterConfig.TarballUploadEntry\x1a\x62\n\x0cTarballEntry\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x14\n\x0coauth_scopes\x18\x02 \x03(\t\x12\x0e\n\x06\x64omain\x18\x03 \x01(\t\x12\x0f\n\x07systems\x18\x04 \x03(\t\x12\x0e\n\x06groups\x18\x05 \x03(\t\x1ap\n\x12TarballUploadEntry\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1b\n\x13\x61uthorized_uploader\x18\x02 \x03(\t\x12\x0e\n\x06\x64omain\x18\x03 \x01(\t\x12\x0f\n\x07systems\x18\x04 \x03(\t\x12\x0e\n\x06groups\x18\x05 \x03(\t\x1aR\n\x0ePlainlistEntry\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x14\n\x0coauth_scopes\x18\x02 \x03(\t\x12\x0e\n\x06\x64omain\x18\x03 \x01(\t\x12\r\n\x05group\x18\x04 \x01(\t\"u\n\x0bOAuthConfig\x12\x19\n\x11primary_client_id\x18\x01 \x01(\t\x12\x1d\n\x15primary_client_secret\x18\x02 \x01(\t\x12\x12\n\nclient_ids\x18\x03 \x03(\t\x12\x18\n\x10token_server_url\x18\x04 \x01(\t\"\x93\x02\n\x11IPWhitelistConfig\x12\x42\n\rip_whitelists\x18\x01 \x03(\x0b\x32+.auth_service.IPWhitelistConfig.IPWhitelist\x12?\n\x0b\x61ssignments\x18\x02 \x03(\x0b\x32*.auth_service.IPWhitelistConfig.Assignment\x1a>\n\x0bIPWhitelist\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07subnets\x18\x02 \x03(\t\x12\x10\n\x08includes\x18\x03 \x03(\t\x1a\x39\n\nAssignment\x12\x10\n\x08identity\x18\x01 \x01(\t\x12\x19\n\x11ip_whitelist_name\x18\x02 \x01(\tb\x06proto3')
)




_SETTINGSCFG = _descriptor.Descriptor(
  name='SettingsCfg',
  full_name='auth_service.SettingsCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable_ts_monitoring', full_name='auth_service.SettingsCfg.enable_ts_monitoring', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth_db_gs_path', full_name='auth_service.SettingsCfg.auth_db_gs_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=98,
)


_GROUPIMPORTERCONFIG_TARBALLENTRY = _descriptor.Descriptor(
  name='TarballEntry',
  full_name='auth_service.GroupImporterConfig.TarballEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='auth_service.GroupImporterConfig.TarballEntry.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oauth_scopes', full_name='auth_service.GroupImporterConfig.TarballEntry.oauth_scopes', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='auth_service.GroupImporterConfig.TarballEntry.domain', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='systems', full_name='auth_service.GroupImporterConfig.TarballEntry.systems', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='groups', full_name='auth_service.GroupImporterConfig.TarballEntry.groups', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=336,
  serialized_end=434,
)

_GROUPIMPORTERCONFIG_TARBALLUPLOADENTRY = _descriptor.Descriptor(
  name='TarballUploadEntry',
  full_name='auth_service.GroupImporterConfig.TarballUploadEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='auth_service.GroupImporterConfig.TarballUploadEntry.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='authorized_uploader', full_name='auth_service.GroupImporterConfig.TarballUploadEntry.authorized_uploader', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='auth_service.GroupImporterConfig.TarballUploadEntry.domain', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='systems', full_name='auth_service.GroupImporterConfig.TarballUploadEntry.systems', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='groups', full_name='auth_service.GroupImporterConfig.TarballUploadEntry.groups', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=436,
  serialized_end=548,
)

_GROUPIMPORTERCONFIG_PLAINLISTENTRY = _descriptor.Descriptor(
  name='PlainlistEntry',
  full_name='auth_service.GroupImporterConfig.PlainlistEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='auth_service.GroupImporterConfig.PlainlistEntry.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oauth_scopes', full_name='auth_service.GroupImporterConfig.PlainlistEntry.oauth_scopes', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain', full_name='auth_service.GroupImporterConfig.PlainlistEntry.domain', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group', full_name='auth_service.GroupImporterConfig.PlainlistEntry.group', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=550,
  serialized_end=632,
)

_GROUPIMPORTERCONFIG = _descriptor.Descriptor(
  name='GroupImporterConfig',
  full_name='auth_service.GroupImporterConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tarball', full_name='auth_service.GroupImporterConfig.tarball', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plainlist', full_name='auth_service.GroupImporterConfig.plainlist', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tarball_upload', full_name='auth_service.GroupImporterConfig.tarball_upload', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GROUPIMPORTERCONFIG_TARBALLENTRY, _GROUPIMPORTERCONFIG_TARBALLUPLOADENTRY, _GROUPIMPORTERCONFIG_PLAINLISTENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=632,
)


_OAUTHCONFIG = _descriptor.Descriptor(
  name='OAuthConfig',
  full_name='auth_service.OAuthConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='primary_client_id', full_name='auth_service.OAuthConfig.primary_client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='primary_client_secret', full_name='auth_service.OAuthConfig.primary_client_secret', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_ids', full_name='auth_service.OAuthConfig.client_ids', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token_server_url', full_name='auth_service.OAuthConfig.token_server_url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=634,
  serialized_end=751,
)


_IPWHITELISTCONFIG_IPWHITELIST = _descriptor.Descriptor(
  name='IPWhitelist',
  full_name='auth_service.IPWhitelistConfig.IPWhitelist',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='auth_service.IPWhitelistConfig.IPWhitelist.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subnets', full_name='auth_service.IPWhitelistConfig.IPWhitelist.subnets', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='includes', full_name='auth_service.IPWhitelistConfig.IPWhitelist.includes', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=908,
  serialized_end=970,
)

_IPWHITELISTCONFIG_ASSIGNMENT = _descriptor.Descriptor(
  name='Assignment',
  full_name='auth_service.IPWhitelistConfig.Assignment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identity', full_name='auth_service.IPWhitelistConfig.Assignment.identity', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip_whitelist_name', full_name='auth_service.IPWhitelistConfig.Assignment.ip_whitelist_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=972,
  serialized_end=1029,
)

_IPWHITELISTCONFIG = _descriptor.Descriptor(
  name='IPWhitelistConfig',
  full_name='auth_service.IPWhitelistConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip_whitelists', full_name='auth_service.IPWhitelistConfig.ip_whitelists', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='assignments', full_name='auth_service.IPWhitelistConfig.assignments', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_IPWHITELISTCONFIG_IPWHITELIST, _IPWHITELISTCONFIG_ASSIGNMENT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=754,
  serialized_end=1029,
)

_GROUPIMPORTERCONFIG_TARBALLENTRY.containing_type = _GROUPIMPORTERCONFIG
_GROUPIMPORTERCONFIG_TARBALLUPLOADENTRY.containing_type = _GROUPIMPORTERCONFIG
_GROUPIMPORTERCONFIG_PLAINLISTENTRY.containing_type = _GROUPIMPORTERCONFIG
_GROUPIMPORTERCONFIG.fields_by_name['tarball'].message_type = _GROUPIMPORTERCONFIG_TARBALLENTRY
_GROUPIMPORTERCONFIG.fields_by_name['plainlist'].message_type = _GROUPIMPORTERCONFIG_PLAINLISTENTRY
_GROUPIMPORTERCONFIG.fields_by_name['tarball_upload'].message_type = _GROUPIMPORTERCONFIG_TARBALLUPLOADENTRY
_IPWHITELISTCONFIG_IPWHITELIST.containing_type = _IPWHITELISTCONFIG
_IPWHITELISTCONFIG_ASSIGNMENT.containing_type = _IPWHITELISTCONFIG
_IPWHITELISTCONFIG.fields_by_name['ip_whitelists'].message_type = _IPWHITELISTCONFIG_IPWHITELIST
_IPWHITELISTCONFIG.fields_by_name['assignments'].message_type = _IPWHITELISTCONFIG_ASSIGNMENT
DESCRIPTOR.message_types_by_name['SettingsCfg'] = _SETTINGSCFG
DESCRIPTOR.message_types_by_name['GroupImporterConfig'] = _GROUPIMPORTERCONFIG
DESCRIPTOR.message_types_by_name['OAuthConfig'] = _OAUTHCONFIG
DESCRIPTOR.message_types_by_name['IPWhitelistConfig'] = _IPWHITELISTCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SettingsCfg = _reflection.GeneratedProtocolMessageType('SettingsCfg', (_message.Message,), dict(
  DESCRIPTOR = _SETTINGSCFG,
  __module__ = 'config_pb2'
  # @@protoc_insertion_point(class_scope:auth_service.SettingsCfg)
  ))
_sym_db.RegisterMessage(SettingsCfg)

GroupImporterConfig = _reflection.GeneratedProtocolMessageType('GroupImporterConfig', (_message.Message,), dict(

  TarballEntry = _reflection.GeneratedProtocolMessageType('TarballEntry', (_message.Message,), dict(
    DESCRIPTOR = _GROUPIMPORTERCONFIG_TARBALLENTRY,
    __module__ = 'config_pb2'
    # @@protoc_insertion_point(class_scope:auth_service.GroupImporterConfig.TarballEntry)
    ))
  ,

  TarballUploadEntry = _reflection.GeneratedProtocolMessageType('TarballUploadEntry', (_message.Message,), dict(
    DESCRIPTOR = _GROUPIMPORTERCONFIG_TARBALLUPLOADENTRY,
    __module__ = 'config_pb2'
    # @@protoc_insertion_point(class_scope:auth_service.GroupImporterConfig.TarballUploadEntry)
    ))
  ,

  PlainlistEntry = _reflection.GeneratedProtocolMessageType('PlainlistEntry', (_message.Message,), dict(
    DESCRIPTOR = _GROUPIMPORTERCONFIG_PLAINLISTENTRY,
    __module__ = 'config_pb2'
    # @@protoc_insertion_point(class_scope:auth_service.GroupImporterConfig.PlainlistEntry)
    ))
  ,
  DESCRIPTOR = _GROUPIMPORTERCONFIG,
  __module__ = 'config_pb2'
  # @@protoc_insertion_point(class_scope:auth_service.GroupImporterConfig)
  ))
_sym_db.RegisterMessage(GroupImporterConfig)
_sym_db.RegisterMessage(GroupImporterConfig.TarballEntry)
_sym_db.RegisterMessage(GroupImporterConfig.TarballUploadEntry)
_sym_db.RegisterMessage(GroupImporterConfig.PlainlistEntry)

OAuthConfig = _reflection.GeneratedProtocolMessageType('OAuthConfig', (_message.Message,), dict(
  DESCRIPTOR = _OAUTHCONFIG,
  __module__ = 'config_pb2'
  # @@protoc_insertion_point(class_scope:auth_service.OAuthConfig)
  ))
_sym_db.RegisterMessage(OAuthConfig)

IPWhitelistConfig = _reflection.GeneratedProtocolMessageType('IPWhitelistConfig', (_message.Message,), dict(

  IPWhitelist = _reflection.GeneratedProtocolMessageType('IPWhitelist', (_message.Message,), dict(
    DESCRIPTOR = _IPWHITELISTCONFIG_IPWHITELIST,
    __module__ = 'config_pb2'
    # @@protoc_insertion_point(class_scope:auth_service.IPWhitelistConfig.IPWhitelist)
    ))
  ,

  Assignment = _reflection.GeneratedProtocolMessageType('Assignment', (_message.Message,), dict(
    DESCRIPTOR = _IPWHITELISTCONFIG_ASSIGNMENT,
    __module__ = 'config_pb2'
    # @@protoc_insertion_point(class_scope:auth_service.IPWhitelistConfig.Assignment)
    ))
  ,
  DESCRIPTOR = _IPWHITELISTCONFIG,
  __module__ = 'config_pb2'
  # @@protoc_insertion_point(class_scope:auth_service.IPWhitelistConfig)
  ))
_sym_db.RegisterMessage(IPWhitelistConfig)
_sym_db.RegisterMessage(IPWhitelistConfig.IPWhitelist)
_sym_db.RegisterMessage(IPWhitelistConfig.Assignment)


# @@protoc_insertion_point(module_scope)
