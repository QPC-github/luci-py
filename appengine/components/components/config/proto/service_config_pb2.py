# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service_config.proto',
  package='luci.config',
  syntax='proto2',
  serialized_pb=_b('\n\x14service_config.proto\x12\x0bluci.config\"\x89\x01\n\x11\x43onfigSetLocation\x12\x0b\n\x03url\x18\x01 \x01(\t\x12@\n\x0cstorage_type\x18\x02 \x01(\x0e\x32*.luci.config.ConfigSetLocation.StorageType\"%\n\x0bStorageType\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07GITILES\x10\x01\"N\n\x07Project\x12\n\n\x02id\x18\x01 \x01(\t\x12\x37\n\x0f\x63onfig_location\x18\x02 \x01(\x0b\x32\x1e.luci.config.ConfigSetLocation\"5\n\x0bProjectsCfg\x12&\n\x08projects\x18\x01 \x03(\x0b\x32\x14.luci.config.Project\"\x84\x01\n\x07Service\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06owners\x18\x02 \x03(\t\x12\x37\n\x0f\x63onfig_location\x18\x03 \x01(\x0b\x32\x1e.luci.config.ConfigSetLocation\x12\x14\n\x0cmetadata_url\x18\x04 \x01(\t\x12\x0e\n\x06\x61\x63\x63\x65ss\x18\x05 \x03(\t\"U\n\x16ServiceDynamicMetadata\x12\x0f\n\x07version\x18\x01 \x01(\t\x12*\n\nvalidation\x18\x02 \x01(\x0b\x32\x16.luci.config.Validator\"5\n\x0bServicesCfg\x12&\n\x08services\x18\x01 \x03(\x0b\x32\x14.luci.config.Service\"w\n\x06\x41\x63lCfg\x12\x1c\n\x14project_access_group\x18\x02 \x01(\t\x12\x13\n\x0b\x61\x64min_group\x18\x03 \x01(\t\x12 \n\x18\x63onfig_get_by_hash_group\x18\x04 \x01(\t\x12\x18\n\x10validation_group\x18\x05 \x01(\t\"\xee\x01\n\tImportCfg\x12/\n\x07gitiles\x18\x01 \x01(\x0b\x32\x1e.luci.config.ImportCfg.Gitiles\x1a\xaf\x01\n\x07Gitiles\x12\x1a\n\x12\x66\x65tch_log_deadline\x18\x01 \x01(\x05\x12\x1e\n\x16\x66\x65tch_archive_deadline\x18\x02 \x01(\x05\x12\"\n\x1aproject_config_default_ref\x18\x03 \x01(\t\x12#\n\x1bproject_config_default_path\x18\x04 \x01(\t\x12\x1f\n\x17ref_config_default_path\x18\x05 \x01(\t\"b\n\nSchemasCfg\x12/\n\x07schemas\x18\x01 \x03(\x0b\x32\x1e.luci.config.SchemasCfg.Schema\x1a#\n\x06Schema\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\"1\n\rConfigPattern\x12\x12\n\nconfig_set\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\"F\n\tValidator\x12,\n\x08patterns\x18\x01 \x03(\x0b\x32\x1a.luci.config.ConfigPattern\x12\x0b\n\x03url\x18\x02 \x01(\t\"M\n\x18ValidationRequestMessage\x12\x12\n\nconfig_set\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\x0c\"\x80\x02\n\x19ValidationResponseMessage\x12@\n\x08messages\x18\x01 \x03(\x0b\x32..luci.config.ValidationResponseMessage.Message\x1aZ\n\x07Message\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x41\n\x08severity\x18\x02 \x01(\x0e\x32/.luci.config.ValidationResponseMessage.Severity\"E\n\x08Severity\x12\t\n\x05\x44\x45\x42UG\x10\n\x12\x08\n\x04INFO\x10\x14\x12\x0b\n\x07WARNING\x10\x1e\x12\t\n\x05\x45RROR\x10(\x12\x0c\n\x08\x43RITICAL\x10\x32')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CONFIGSETLOCATION_STORAGETYPE = _descriptor.EnumDescriptor(
  name='StorageType',
  full_name='luci.config.ConfigSetLocation.StorageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GITILES', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=138,
  serialized_end=175,
)
_sym_db.RegisterEnumDescriptor(_CONFIGSETLOCATION_STORAGETYPE)

_VALIDATIONRESPONSEMESSAGE_SEVERITY = _descriptor.EnumDescriptor(
  name='Severity',
  full_name='luci.config.ValidationResponseMessage.Severity',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEBUG', index=0, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INFO', index=1, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING', index=2, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=3, number=40,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRITICAL', index=4, number=50,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1441,
  serialized_end=1510,
)
_sym_db.RegisterEnumDescriptor(_VALIDATIONRESPONSEMESSAGE_SEVERITY)


_CONFIGSETLOCATION = _descriptor.Descriptor(
  name='ConfigSetLocation',
  full_name='luci.config.ConfigSetLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='luci.config.ConfigSetLocation.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='storage_type', full_name='luci.config.ConfigSetLocation.storage_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONFIGSETLOCATION_STORAGETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=175,
)


_PROJECT = _descriptor.Descriptor(
  name='Project',
  full_name='luci.config.Project',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='luci.config.Project.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='config_location', full_name='luci.config.Project.config_location', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=177,
  serialized_end=255,
)


_PROJECTSCFG = _descriptor.Descriptor(
  name='ProjectsCfg',
  full_name='luci.config.ProjectsCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='projects', full_name='luci.config.ProjectsCfg.projects', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=257,
  serialized_end=310,
)


_SERVICE = _descriptor.Descriptor(
  name='Service',
  full_name='luci.config.Service',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='luci.config.Service.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='owners', full_name='luci.config.Service.owners', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='config_location', full_name='luci.config.Service.config_location', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata_url', full_name='luci.config.Service.metadata_url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='access', full_name='luci.config.Service.access', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=313,
  serialized_end=445,
)


_SERVICEDYNAMICMETADATA = _descriptor.Descriptor(
  name='ServiceDynamicMetadata',
  full_name='luci.config.ServiceDynamicMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='luci.config.ServiceDynamicMetadata.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='validation', full_name='luci.config.ServiceDynamicMetadata.validation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=447,
  serialized_end=532,
)


_SERVICESCFG = _descriptor.Descriptor(
  name='ServicesCfg',
  full_name='luci.config.ServicesCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='services', full_name='luci.config.ServicesCfg.services', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=534,
  serialized_end=587,
)


_ACLCFG = _descriptor.Descriptor(
  name='AclCfg',
  full_name='luci.config.AclCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_access_group', full_name='luci.config.AclCfg.project_access_group', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='admin_group', full_name='luci.config.AclCfg.admin_group', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='config_get_by_hash_group', full_name='luci.config.AclCfg.config_get_by_hash_group', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='validation_group', full_name='luci.config.AclCfg.validation_group', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=589,
  serialized_end=708,
)


_IMPORTCFG_GITILES = _descriptor.Descriptor(
  name='Gitiles',
  full_name='luci.config.ImportCfg.Gitiles',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fetch_log_deadline', full_name='luci.config.ImportCfg.Gitiles.fetch_log_deadline', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fetch_archive_deadline', full_name='luci.config.ImportCfg.Gitiles.fetch_archive_deadline', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='project_config_default_ref', full_name='luci.config.ImportCfg.Gitiles.project_config_default_ref', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='project_config_default_path', full_name='luci.config.ImportCfg.Gitiles.project_config_default_path', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ref_config_default_path', full_name='luci.config.ImportCfg.Gitiles.ref_config_default_path', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=774,
  serialized_end=949,
)

_IMPORTCFG = _descriptor.Descriptor(
  name='ImportCfg',
  full_name='luci.config.ImportCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gitiles', full_name='luci.config.ImportCfg.gitiles', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_IMPORTCFG_GITILES, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=711,
  serialized_end=949,
)


_SCHEMASCFG_SCHEMA = _descriptor.Descriptor(
  name='Schema',
  full_name='luci.config.SchemasCfg.Schema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='luci.config.SchemasCfg.Schema.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='luci.config.SchemasCfg.Schema.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1014,
  serialized_end=1049,
)

_SCHEMASCFG = _descriptor.Descriptor(
  name='SchemasCfg',
  full_name='luci.config.SchemasCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schemas', full_name='luci.config.SchemasCfg.schemas', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SCHEMASCFG_SCHEMA, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=951,
  serialized_end=1049,
)


_CONFIGPATTERN = _descriptor.Descriptor(
  name='ConfigPattern',
  full_name='luci.config.ConfigPattern',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config_set', full_name='luci.config.ConfigPattern.config_set', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='luci.config.ConfigPattern.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1051,
  serialized_end=1100,
)


_VALIDATOR = _descriptor.Descriptor(
  name='Validator',
  full_name='luci.config.Validator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='patterns', full_name='luci.config.Validator.patterns', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='luci.config.Validator.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1102,
  serialized_end=1172,
)


_VALIDATIONREQUESTMESSAGE = _descriptor.Descriptor(
  name='ValidationRequestMessage',
  full_name='luci.config.ValidationRequestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config_set', full_name='luci.config.ValidationRequestMessage.config_set', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='luci.config.ValidationRequestMessage.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='luci.config.ValidationRequestMessage.content', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1174,
  serialized_end=1251,
)


_VALIDATIONRESPONSEMESSAGE_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='luci.config.ValidationResponseMessage.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='luci.config.ValidationResponseMessage.Message.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='severity', full_name='luci.config.ValidationResponseMessage.Message.severity', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=10,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1349,
  serialized_end=1439,
)

_VALIDATIONRESPONSEMESSAGE = _descriptor.Descriptor(
  name='ValidationResponseMessage',
  full_name='luci.config.ValidationResponseMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messages', full_name='luci.config.ValidationResponseMessage.messages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_VALIDATIONRESPONSEMESSAGE_MESSAGE, ],
  enum_types=[
    _VALIDATIONRESPONSEMESSAGE_SEVERITY,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1254,
  serialized_end=1510,
)

_CONFIGSETLOCATION.fields_by_name['storage_type'].enum_type = _CONFIGSETLOCATION_STORAGETYPE
_CONFIGSETLOCATION_STORAGETYPE.containing_type = _CONFIGSETLOCATION
_PROJECT.fields_by_name['config_location'].message_type = _CONFIGSETLOCATION
_PROJECTSCFG.fields_by_name['projects'].message_type = _PROJECT
_SERVICE.fields_by_name['config_location'].message_type = _CONFIGSETLOCATION
_SERVICEDYNAMICMETADATA.fields_by_name['validation'].message_type = _VALIDATOR
_SERVICESCFG.fields_by_name['services'].message_type = _SERVICE
_IMPORTCFG_GITILES.containing_type = _IMPORTCFG
_IMPORTCFG.fields_by_name['gitiles'].message_type = _IMPORTCFG_GITILES
_SCHEMASCFG_SCHEMA.containing_type = _SCHEMASCFG
_SCHEMASCFG.fields_by_name['schemas'].message_type = _SCHEMASCFG_SCHEMA
_VALIDATOR.fields_by_name['patterns'].message_type = _CONFIGPATTERN
_VALIDATIONRESPONSEMESSAGE_MESSAGE.fields_by_name['severity'].enum_type = _VALIDATIONRESPONSEMESSAGE_SEVERITY
_VALIDATIONRESPONSEMESSAGE_MESSAGE.containing_type = _VALIDATIONRESPONSEMESSAGE
_VALIDATIONRESPONSEMESSAGE.fields_by_name['messages'].message_type = _VALIDATIONRESPONSEMESSAGE_MESSAGE
_VALIDATIONRESPONSEMESSAGE_SEVERITY.containing_type = _VALIDATIONRESPONSEMESSAGE
DESCRIPTOR.message_types_by_name['ConfigSetLocation'] = _CONFIGSETLOCATION
DESCRIPTOR.message_types_by_name['Project'] = _PROJECT
DESCRIPTOR.message_types_by_name['ProjectsCfg'] = _PROJECTSCFG
DESCRIPTOR.message_types_by_name['Service'] = _SERVICE
DESCRIPTOR.message_types_by_name['ServiceDynamicMetadata'] = _SERVICEDYNAMICMETADATA
DESCRIPTOR.message_types_by_name['ServicesCfg'] = _SERVICESCFG
DESCRIPTOR.message_types_by_name['AclCfg'] = _ACLCFG
DESCRIPTOR.message_types_by_name['ImportCfg'] = _IMPORTCFG
DESCRIPTOR.message_types_by_name['SchemasCfg'] = _SCHEMASCFG
DESCRIPTOR.message_types_by_name['ConfigPattern'] = _CONFIGPATTERN
DESCRIPTOR.message_types_by_name['Validator'] = _VALIDATOR
DESCRIPTOR.message_types_by_name['ValidationRequestMessage'] = _VALIDATIONREQUESTMESSAGE
DESCRIPTOR.message_types_by_name['ValidationResponseMessage'] = _VALIDATIONRESPONSEMESSAGE

ConfigSetLocation = _reflection.GeneratedProtocolMessageType('ConfigSetLocation', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGSETLOCATION,
  __module__ = 'service_config_pb2'
  # @@protoc_insertion_point(class_scope:luci.config.ConfigSetLocation)
  ))
_sym_db.RegisterMessage(ConfigSetLocation)

Project = _reflection.GeneratedProtocolMessageType('Project', (_message.Message,), dict(
  DESCRIPTOR = _PROJECT,
  __module__ = 'service_config_pb2'
  # @@protoc_insertion_point(class_scope:luci.config.Project)
  ))
_sym_db.RegisterMessage(Project)

ProjectsCfg = _reflection.GeneratedProtocolMessageType('ProjectsCfg', (_message.Message,), dict(
  DESCRIPTOR = _PROJECTSCFG,
  __module__ = 'service_config_pb2'
  # @@protoc_insertion_point(class_scope:luci.config.ProjectsCfg)
  ))
_sym_db.RegisterMessage(ProjectsCfg)

Service = _reflection.GeneratedProtocolMessageType('Service', (_message.Message,), dict(
  DESCRIPTOR = _SERVICE,
  __module__ = 'service_config_pb2'
  # @@protoc_insertion_point(class_scope:luci.config.Service)
  ))
_sym_db.RegisterMessage(Service)

ServiceDynamicMetadata = _reflection.GeneratedProtocolMessageType('ServiceDynamicMetadata', (_message.Message,), dict(
  DESCRIPTOR = _SERVICEDYNAMICMETADATA,
  __module__ = 'service_config_pb2'
  # @@protoc_insertion_point(class_scope:luci.config.ServiceDynamicMetadata)
  ))
_sym_db.RegisterMessage(ServiceDynamicMetadata)

ServicesCfg = _reflection.GeneratedProtocolMessageType('ServicesCfg', (_message.Message,), dict(
  DESCRIPTOR = _SERVICESCFG,
  __module__ = 'service_config_pb2'
  # @@protoc_insertion_point(class_scope:luci.config.ServicesCfg)
  ))
_sym_db.RegisterMessage(ServicesCfg)

AclCfg = _reflection.GeneratedProtocolMessageType('AclCfg', (_message.Message,), dict(
  DESCRIPTOR = _ACLCFG,
  __module__ = 'service_config_pb2'
  # @@protoc_insertion_point(class_scope:luci.config.AclCfg)
  ))
_sym_db.RegisterMessage(AclCfg)

ImportCfg = _reflection.GeneratedProtocolMessageType('ImportCfg', (_message.Message,), dict(

  Gitiles = _reflection.GeneratedProtocolMessageType('Gitiles', (_message.Message,), dict(
    DESCRIPTOR = _IMPORTCFG_GITILES,
    __module__ = 'service_config_pb2'
    # @@protoc_insertion_point(class_scope:luci.config.ImportCfg.Gitiles)
    ))
  ,
  DESCRIPTOR = _IMPORTCFG,
  __module__ = 'service_config_pb2'
  # @@protoc_insertion_point(class_scope:luci.config.ImportCfg)
  ))
_sym_db.RegisterMessage(ImportCfg)
_sym_db.RegisterMessage(ImportCfg.Gitiles)

SchemasCfg = _reflection.GeneratedProtocolMessageType('SchemasCfg', (_message.Message,), dict(

  Schema = _reflection.GeneratedProtocolMessageType('Schema', (_message.Message,), dict(
    DESCRIPTOR = _SCHEMASCFG_SCHEMA,
    __module__ = 'service_config_pb2'
    # @@protoc_insertion_point(class_scope:luci.config.SchemasCfg.Schema)
    ))
  ,
  DESCRIPTOR = _SCHEMASCFG,
  __module__ = 'service_config_pb2'
  # @@protoc_insertion_point(class_scope:luci.config.SchemasCfg)
  ))
_sym_db.RegisterMessage(SchemasCfg)
_sym_db.RegisterMessage(SchemasCfg.Schema)

ConfigPattern = _reflection.GeneratedProtocolMessageType('ConfigPattern', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGPATTERN,
  __module__ = 'service_config_pb2'
  # @@protoc_insertion_point(class_scope:luci.config.ConfigPattern)
  ))
_sym_db.RegisterMessage(ConfigPattern)

Validator = _reflection.GeneratedProtocolMessageType('Validator', (_message.Message,), dict(
  DESCRIPTOR = _VALIDATOR,
  __module__ = 'service_config_pb2'
  # @@protoc_insertion_point(class_scope:luci.config.Validator)
  ))
_sym_db.RegisterMessage(Validator)

ValidationRequestMessage = _reflection.GeneratedProtocolMessageType('ValidationRequestMessage', (_message.Message,), dict(
  DESCRIPTOR = _VALIDATIONREQUESTMESSAGE,
  __module__ = 'service_config_pb2'
  # @@protoc_insertion_point(class_scope:luci.config.ValidationRequestMessage)
  ))
_sym_db.RegisterMessage(ValidationRequestMessage)

ValidationResponseMessage = _reflection.GeneratedProtocolMessageType('ValidationResponseMessage', (_message.Message,), dict(

  Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
    DESCRIPTOR = _VALIDATIONRESPONSEMESSAGE_MESSAGE,
    __module__ = 'service_config_pb2'
    # @@protoc_insertion_point(class_scope:luci.config.ValidationResponseMessage.Message)
    ))
  ,
  DESCRIPTOR = _VALIDATIONRESPONSEMESSAGE,
  __module__ = 'service_config_pb2'
  # @@protoc_insertion_point(class_scope:luci.config.ValidationResponseMessage)
  ))
_sym_db.RegisterMessage(ValidationResponseMessage)
_sym_db.RegisterMessage(ValidationResponseMessage.Message)


# @@protoc_insertion_point(module_scope)
