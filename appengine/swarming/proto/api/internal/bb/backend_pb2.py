# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: backend.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import launcher_pb2 as launcher__pb2
import common_pb2 as common__pb2
import swarming_bb_pb2 as swarming__bb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='backend.proto',
  package='swarming.backend',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rbackend.proto\x12\x10swarming.backend\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0elauncher.proto\x1a\x0c\x63ommon.proto\x1a\x11swarming_bb.proto\"\xba\x06\n\x0eRunTaskRequest\x12\x0e\n\x06target\x18\x01 \x01(\t\x12\x15\n\rbackend_token\x18\x02 \x01(\t\x12\r\n\x05realm\x18\x03 \x01(\t\x12?\n\x05\x61gent\x18\x04 \x01(\x0b\x32\x30.swarming.backend.RunTaskRequest.AgentExecutable\x12\x12\n\nagent_args\x18\x05 \x03(\t\x12!\n\x07secrets\x18\x06 \x01(\x0b\x32\x10.bb.BuildSecrets\x12\x18\n\x10\x62uildbucket_host\x18\x07 \x01(\t\x12\x10\n\x08\x62uild_id\x18\x08 \x01(\t\x12*\n\ndimensions\x18\t \x03(\x0b\x32\x16.bb.RequestedDimension\x12\x32\n\x0estart_deadline\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x11\x65xecution_timeout\x18\x0b \x01(\x0b\x32\x19.google.protobuf.Duration\x12/\n\x0cgrace_period\x18\x0c \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x1e\n\x06\x63\x61\x63hes\x18\r \x03(\x0b\x32\x0e.bb.CacheEntry\x12/\n\x0e\x62\x61\x63kend_config\x18\x0e \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x13\n\x0b\x65xperiments\x18\x0f \x03(\t\x12\x12\n\nrequest_id\x18\x10 \x01(\t\x1a\x8c\x02\n\x0f\x41gentExecutable\x12L\n\x06source\x18\x01 \x03(\x0b\x32<.swarming.backend.RunTaskRequest.AgentExecutable.SourceEntry\x1a>\n\x0b\x41gentSource\x12\x0e\n\x06sha256\x18\x01 \x01(\t\x12\x12\n\nsize_bytes\x18\x02 \x01(\x03\x12\x0b\n\x03url\x18\x03 \x01(\t\x1ak\n\x0bSourceEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12K\n\x05value\x18\x02 \x01(\x0b\x32<.swarming.backend.RunTaskRequest.AgentExecutable.AgentSource:\x02\x38\x01\"?\n\x11\x46\x65tchTasksRequest\x12*\n\x08task_ids\x18\x01 \x03(\x0b\x32\x18.swarming.backend.TaskID\";\n\x12\x46\x65tchTasksResponse\x12%\n\x05tasks\x18\x01 \x03(\x0b\x32\x16.swarming.backend.Task\"@\n\x12\x43\x61ncelTasksRequest\x12*\n\x08task_ids\x18\x01 \x03(\x0b\x32\x18.swarming.backend.TaskID\"<\n\x13\x43\x61ncelTasksResponse\x12%\n\x05tasks\x18\x01 \x03(\x0b\x32\x16.swarming.backend.Task\"\xb0\x01\n\x16ValidateConfigsRequest\x12G\n\x07\x63onfigs\x18\x01 \x03(\x0b\x32\x36.swarming.backend.ValidateConfigsRequest.ConfigContext\x1aM\n\rConfigContext\x12\x0e\n\x06target\x18\x01 \x01(\t\x12,\n\x0b\x63onfig_json\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"\x94\x01\n\x17ValidateConfigsResponse\x12L\n\rconfig_errors\x18\x01 \x03(\x0b\x32\x35.swarming.backend.ValidateConfigsResponse.ErrorDetail\x1a+\n\x0b\x45rrorDetail\x12\r\n\x05index\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"\xc1\x01\n\x04Task\x12$\n\x02id\x18\x01 \x01(\x0b\x32\x18.swarming.backend.TaskID\x12\x0c\n\x04link\x18\x02 \x01(\t\x12\x1a\n\x06status\x18\x03 \x01(\x0e\x32\n.bb.Status\x12)\n\x0estatus_details\x18\x04 \x01(\x0b\x32\x11.bb.StatusDetails\x12\x14\n\x0csummary_html\x18\x05 \x01(\t\x12(\n\x07\x64\x65tails\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\"$\n\x06TaskID\x12\x0e\n\x06target\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t2\xf7\x02\n\x0bTaskBackend\x12\x45\n\x07RunTask\x12 .swarming.backend.RunTaskRequest\x1a\x16.google.protobuf.Empty\"\x00\x12Y\n\nFetchTasks\x12#.swarming.backend.FetchTasksRequest\x1a$.swarming.backend.FetchTasksResponse\"\x00\x12\\\n\x0b\x43\x61ncelTasks\x12$.swarming.backend.CancelTasksRequest\x1a%.swarming.backend.CancelTasksResponse\"\x00\x12h\n\x0fValidateConfigs\x12(.swarming.backend.ValidateConfigsRequest\x1a).swarming.backend.ValidateConfigsResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,launcher__pb2.DESCRIPTOR,common__pb2.DESCRIPTOR,swarming__bb__pb2.DESCRIPTOR,])




_RUNTASKREQUEST_AGENTEXECUTABLE_AGENTSOURCE = _descriptor.Descriptor(
  name='AgentSource',
  full_name='swarming.backend.RunTaskRequest.AgentExecutable.AgentSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sha256', full_name='swarming.backend.RunTaskRequest.AgentExecutable.AgentSource.sha256', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size_bytes', full_name='swarming.backend.RunTaskRequest.AgentExecutable.AgentSource.size_bytes', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='swarming.backend.RunTaskRequest.AgentExecutable.AgentSource.url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=864,
  serialized_end=926,
)

_RUNTASKREQUEST_AGENTEXECUTABLE_SOURCEENTRY = _descriptor.Descriptor(
  name='SourceEntry',
  full_name='swarming.backend.RunTaskRequest.AgentExecutable.SourceEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='swarming.backend.RunTaskRequest.AgentExecutable.SourceEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='swarming.backend.RunTaskRequest.AgentExecutable.SourceEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=928,
  serialized_end=1035,
)

_RUNTASKREQUEST_AGENTEXECUTABLE = _descriptor.Descriptor(
  name='AgentExecutable',
  full_name='swarming.backend.RunTaskRequest.AgentExecutable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='swarming.backend.RunTaskRequest.AgentExecutable.source', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RUNTASKREQUEST_AGENTEXECUTABLE_AGENTSOURCE, _RUNTASKREQUEST_AGENTEXECUTABLE_SOURCEENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=767,
  serialized_end=1035,
)

_RUNTASKREQUEST = _descriptor.Descriptor(
  name='RunTaskRequest',
  full_name='swarming.backend.RunTaskRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='swarming.backend.RunTaskRequest.target', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='backend_token', full_name='swarming.backend.RunTaskRequest.backend_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='realm', full_name='swarming.backend.RunTaskRequest.realm', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='agent', full_name='swarming.backend.RunTaskRequest.agent', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='agent_args', full_name='swarming.backend.RunTaskRequest.agent_args', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secrets', full_name='swarming.backend.RunTaskRequest.secrets', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buildbucket_host', full_name='swarming.backend.RunTaskRequest.buildbucket_host', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='build_id', full_name='swarming.backend.RunTaskRequest.build_id', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='swarming.backend.RunTaskRequest.dimensions', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_deadline', full_name='swarming.backend.RunTaskRequest.start_deadline', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='execution_timeout', full_name='swarming.backend.RunTaskRequest.execution_timeout', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grace_period', full_name='swarming.backend.RunTaskRequest.grace_period', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='caches', full_name='swarming.backend.RunTaskRequest.caches', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='backend_config', full_name='swarming.backend.RunTaskRequest.backend_config', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='experiments', full_name='swarming.backend.RunTaskRequest.experiments', index=14,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='swarming.backend.RunTaskRequest.request_id', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RUNTASKREQUEST_AGENTEXECUTABLE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=1035,
)


_FETCHTASKSREQUEST = _descriptor.Descriptor(
  name='FetchTasksRequest',
  full_name='swarming.backend.FetchTasksRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_ids', full_name='swarming.backend.FetchTasksRequest.task_ids', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1037,
  serialized_end=1100,
)


_FETCHTASKSRESPONSE = _descriptor.Descriptor(
  name='FetchTasksResponse',
  full_name='swarming.backend.FetchTasksResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tasks', full_name='swarming.backend.FetchTasksResponse.tasks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1102,
  serialized_end=1161,
)


_CANCELTASKSREQUEST = _descriptor.Descriptor(
  name='CancelTasksRequest',
  full_name='swarming.backend.CancelTasksRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_ids', full_name='swarming.backend.CancelTasksRequest.task_ids', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1163,
  serialized_end=1227,
)


_CANCELTASKSRESPONSE = _descriptor.Descriptor(
  name='CancelTasksResponse',
  full_name='swarming.backend.CancelTasksResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tasks', full_name='swarming.backend.CancelTasksResponse.tasks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1229,
  serialized_end=1289,
)


_VALIDATECONFIGSREQUEST_CONFIGCONTEXT = _descriptor.Descriptor(
  name='ConfigContext',
  full_name='swarming.backend.ValidateConfigsRequest.ConfigContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='swarming.backend.ValidateConfigsRequest.ConfigContext.target', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config_json', full_name='swarming.backend.ValidateConfigsRequest.ConfigContext.config_json', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1391,
  serialized_end=1468,
)

_VALIDATECONFIGSREQUEST = _descriptor.Descriptor(
  name='ValidateConfigsRequest',
  full_name='swarming.backend.ValidateConfigsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='configs', full_name='swarming.backend.ValidateConfigsRequest.configs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_VALIDATECONFIGSREQUEST_CONFIGCONTEXT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1292,
  serialized_end=1468,
)


_VALIDATECONFIGSRESPONSE_ERRORDETAIL = _descriptor.Descriptor(
  name='ErrorDetail',
  full_name='swarming.backend.ValidateConfigsResponse.ErrorDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='swarming.backend.ValidateConfigsResponse.ErrorDetail.index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='swarming.backend.ValidateConfigsResponse.ErrorDetail.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1576,
  serialized_end=1619,
)

_VALIDATECONFIGSRESPONSE = _descriptor.Descriptor(
  name='ValidateConfigsResponse',
  full_name='swarming.backend.ValidateConfigsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='config_errors', full_name='swarming.backend.ValidateConfigsResponse.config_errors', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_VALIDATECONFIGSRESPONSE_ERRORDETAIL, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1471,
  serialized_end=1619,
)


_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='swarming.backend.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='swarming.backend.Task.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='link', full_name='swarming.backend.Task.link', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='swarming.backend.Task.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status_details', full_name='swarming.backend.Task.status_details', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='summary_html', full_name='swarming.backend.Task.summary_html', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='details', full_name='swarming.backend.Task.details', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1622,
  serialized_end=1815,
)


_TASKID = _descriptor.Descriptor(
  name='TaskID',
  full_name='swarming.backend.TaskID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='swarming.backend.TaskID.target', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='swarming.backend.TaskID.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1817,
  serialized_end=1853,
)

_RUNTASKREQUEST_AGENTEXECUTABLE_AGENTSOURCE.containing_type = _RUNTASKREQUEST_AGENTEXECUTABLE
_RUNTASKREQUEST_AGENTEXECUTABLE_SOURCEENTRY.fields_by_name['value'].message_type = _RUNTASKREQUEST_AGENTEXECUTABLE_AGENTSOURCE
_RUNTASKREQUEST_AGENTEXECUTABLE_SOURCEENTRY.containing_type = _RUNTASKREQUEST_AGENTEXECUTABLE
_RUNTASKREQUEST_AGENTEXECUTABLE.fields_by_name['source'].message_type = _RUNTASKREQUEST_AGENTEXECUTABLE_SOURCEENTRY
_RUNTASKREQUEST_AGENTEXECUTABLE.containing_type = _RUNTASKREQUEST
_RUNTASKREQUEST.fields_by_name['agent'].message_type = _RUNTASKREQUEST_AGENTEXECUTABLE
_RUNTASKREQUEST.fields_by_name['secrets'].message_type = launcher__pb2._BUILDSECRETS
_RUNTASKREQUEST.fields_by_name['dimensions'].message_type = common__pb2._REQUESTEDDIMENSION
_RUNTASKREQUEST.fields_by_name['start_deadline'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_RUNTASKREQUEST.fields_by_name['execution_timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_RUNTASKREQUEST.fields_by_name['grace_period'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_RUNTASKREQUEST.fields_by_name['caches'].message_type = swarming__bb__pb2._CACHEENTRY
_RUNTASKREQUEST.fields_by_name['backend_config'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_FETCHTASKSREQUEST.fields_by_name['task_ids'].message_type = _TASKID
_FETCHTASKSRESPONSE.fields_by_name['tasks'].message_type = _TASK
_CANCELTASKSREQUEST.fields_by_name['task_ids'].message_type = _TASKID
_CANCELTASKSRESPONSE.fields_by_name['tasks'].message_type = _TASK
_VALIDATECONFIGSREQUEST_CONFIGCONTEXT.fields_by_name['config_json'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_VALIDATECONFIGSREQUEST_CONFIGCONTEXT.containing_type = _VALIDATECONFIGSREQUEST
_VALIDATECONFIGSREQUEST.fields_by_name['configs'].message_type = _VALIDATECONFIGSREQUEST_CONFIGCONTEXT
_VALIDATECONFIGSRESPONSE_ERRORDETAIL.containing_type = _VALIDATECONFIGSRESPONSE
_VALIDATECONFIGSRESPONSE.fields_by_name['config_errors'].message_type = _VALIDATECONFIGSRESPONSE_ERRORDETAIL
_TASK.fields_by_name['id'].message_type = _TASKID
_TASK.fields_by_name['status'].enum_type = common__pb2._STATUS
_TASK.fields_by_name['status_details'].message_type = common__pb2._STATUSDETAILS
_TASK.fields_by_name['details'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['RunTaskRequest'] = _RUNTASKREQUEST
DESCRIPTOR.message_types_by_name['FetchTasksRequest'] = _FETCHTASKSREQUEST
DESCRIPTOR.message_types_by_name['FetchTasksResponse'] = _FETCHTASKSRESPONSE
DESCRIPTOR.message_types_by_name['CancelTasksRequest'] = _CANCELTASKSREQUEST
DESCRIPTOR.message_types_by_name['CancelTasksResponse'] = _CANCELTASKSRESPONSE
DESCRIPTOR.message_types_by_name['ValidateConfigsRequest'] = _VALIDATECONFIGSREQUEST
DESCRIPTOR.message_types_by_name['ValidateConfigsResponse'] = _VALIDATECONFIGSRESPONSE
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['TaskID'] = _TASKID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RunTaskRequest = _reflection.GeneratedProtocolMessageType('RunTaskRequest', (_message.Message,), {

  'AgentExecutable' : _reflection.GeneratedProtocolMessageType('AgentExecutable', (_message.Message,), {

    'AgentSource' : _reflection.GeneratedProtocolMessageType('AgentSource', (_message.Message,), {
      'DESCRIPTOR' : _RUNTASKREQUEST_AGENTEXECUTABLE_AGENTSOURCE,
      '__module__' : 'backend_pb2'
      # @@protoc_insertion_point(class_scope:swarming.backend.RunTaskRequest.AgentExecutable.AgentSource)
      })
    ,

    'SourceEntry' : _reflection.GeneratedProtocolMessageType('SourceEntry', (_message.Message,), {
      'DESCRIPTOR' : _RUNTASKREQUEST_AGENTEXECUTABLE_SOURCEENTRY,
      '__module__' : 'backend_pb2'
      # @@protoc_insertion_point(class_scope:swarming.backend.RunTaskRequest.AgentExecutable.SourceEntry)
      })
    ,
    'DESCRIPTOR' : _RUNTASKREQUEST_AGENTEXECUTABLE,
    '__module__' : 'backend_pb2'
    # @@protoc_insertion_point(class_scope:swarming.backend.RunTaskRequest.AgentExecutable)
    })
  ,
  'DESCRIPTOR' : _RUNTASKREQUEST,
  '__module__' : 'backend_pb2'
  # @@protoc_insertion_point(class_scope:swarming.backend.RunTaskRequest)
  })
_sym_db.RegisterMessage(RunTaskRequest)
_sym_db.RegisterMessage(RunTaskRequest.AgentExecutable)
_sym_db.RegisterMessage(RunTaskRequest.AgentExecutable.AgentSource)
_sym_db.RegisterMessage(RunTaskRequest.AgentExecutable.SourceEntry)

FetchTasksRequest = _reflection.GeneratedProtocolMessageType('FetchTasksRequest', (_message.Message,), {
  'DESCRIPTOR' : _FETCHTASKSREQUEST,
  '__module__' : 'backend_pb2'
  # @@protoc_insertion_point(class_scope:swarming.backend.FetchTasksRequest)
  })
_sym_db.RegisterMessage(FetchTasksRequest)

FetchTasksResponse = _reflection.GeneratedProtocolMessageType('FetchTasksResponse', (_message.Message,), {
  'DESCRIPTOR' : _FETCHTASKSRESPONSE,
  '__module__' : 'backend_pb2'
  # @@protoc_insertion_point(class_scope:swarming.backend.FetchTasksResponse)
  })
_sym_db.RegisterMessage(FetchTasksResponse)

CancelTasksRequest = _reflection.GeneratedProtocolMessageType('CancelTasksRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELTASKSREQUEST,
  '__module__' : 'backend_pb2'
  # @@protoc_insertion_point(class_scope:swarming.backend.CancelTasksRequest)
  })
_sym_db.RegisterMessage(CancelTasksRequest)

CancelTasksResponse = _reflection.GeneratedProtocolMessageType('CancelTasksResponse', (_message.Message,), {
  'DESCRIPTOR' : _CANCELTASKSRESPONSE,
  '__module__' : 'backend_pb2'
  # @@protoc_insertion_point(class_scope:swarming.backend.CancelTasksResponse)
  })
_sym_db.RegisterMessage(CancelTasksResponse)

ValidateConfigsRequest = _reflection.GeneratedProtocolMessageType('ValidateConfigsRequest', (_message.Message,), {

  'ConfigContext' : _reflection.GeneratedProtocolMessageType('ConfigContext', (_message.Message,), {
    'DESCRIPTOR' : _VALIDATECONFIGSREQUEST_CONFIGCONTEXT,
    '__module__' : 'backend_pb2'
    # @@protoc_insertion_point(class_scope:swarming.backend.ValidateConfigsRequest.ConfigContext)
    })
  ,
  'DESCRIPTOR' : _VALIDATECONFIGSREQUEST,
  '__module__' : 'backend_pb2'
  # @@protoc_insertion_point(class_scope:swarming.backend.ValidateConfigsRequest)
  })
_sym_db.RegisterMessage(ValidateConfigsRequest)
_sym_db.RegisterMessage(ValidateConfigsRequest.ConfigContext)

ValidateConfigsResponse = _reflection.GeneratedProtocolMessageType('ValidateConfigsResponse', (_message.Message,), {

  'ErrorDetail' : _reflection.GeneratedProtocolMessageType('ErrorDetail', (_message.Message,), {
    'DESCRIPTOR' : _VALIDATECONFIGSRESPONSE_ERRORDETAIL,
    '__module__' : 'backend_pb2'
    # @@protoc_insertion_point(class_scope:swarming.backend.ValidateConfigsResponse.ErrorDetail)
    })
  ,
  'DESCRIPTOR' : _VALIDATECONFIGSRESPONSE,
  '__module__' : 'backend_pb2'
  # @@protoc_insertion_point(class_scope:swarming.backend.ValidateConfigsResponse)
  })
_sym_db.RegisterMessage(ValidateConfigsResponse)
_sym_db.RegisterMessage(ValidateConfigsResponse.ErrorDetail)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), {
  'DESCRIPTOR' : _TASK,
  '__module__' : 'backend_pb2'
  # @@protoc_insertion_point(class_scope:swarming.backend.Task)
  })
_sym_db.RegisterMessage(Task)

TaskID = _reflection.GeneratedProtocolMessageType('TaskID', (_message.Message,), {
  'DESCRIPTOR' : _TASKID,
  '__module__' : 'backend_pb2'
  # @@protoc_insertion_point(class_scope:swarming.backend.TaskID)
  })
_sym_db.RegisterMessage(TaskID)


_RUNTASKREQUEST_AGENTEXECUTABLE_SOURCEENTRY._options = None

_TASKBACKEND = _descriptor.ServiceDescriptor(
  name='TaskBackend',
  full_name='swarming.backend.TaskBackend',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1856,
  serialized_end=2231,
  methods=[
  _descriptor.MethodDescriptor(
    name='RunTask',
    full_name='swarming.backend.TaskBackend.RunTask',
    index=0,
    containing_service=None,
    input_type=_RUNTASKREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FetchTasks',
    full_name='swarming.backend.TaskBackend.FetchTasks',
    index=1,
    containing_service=None,
    input_type=_FETCHTASKSREQUEST,
    output_type=_FETCHTASKSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CancelTasks',
    full_name='swarming.backend.TaskBackend.CancelTasks',
    index=2,
    containing_service=None,
    input_type=_CANCELTASKSREQUEST,
    output_type=_CANCELTASKSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ValidateConfigs',
    full_name='swarming.backend.TaskBackend.ValidateConfigs',
    index=3,
    containing_service=None,
    input_type=_VALIDATECONFIGSREQUEST,
    output_type=_VALIDATECONFIGSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TASKBACKEND)

DESCRIPTOR.services_by_name['TaskBackend'] = _TASKBACKEND

# @@protoc_insertion_point(module_scope)
