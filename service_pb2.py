# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rservice.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\"&\n\rNumberSquared\x12\x15\n\rnumberSquared\x18\x01 \x01(\x03\x32\\\n\rSquareService\x12K\n\x0cSquareNumber\x12\x16.google.protobuf.Empty\x1a\x0e.NumberSquared\"\x13\x82\xd3\xe4\x93\x02\r\x12\x0b/v1/numbersb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_NUMBERSQUARED = _descriptor.Descriptor(
  name='NumberSquared',
  full_name='NumberSquared',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='numberSquared', full_name='NumberSquared.numberSquared', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=114,
)

DESCRIPTOR.message_types_by_name['NumberSquared'] = _NUMBERSQUARED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NumberSquared = _reflection.GeneratedProtocolMessageType('NumberSquared', (_message.Message,), dict(
  DESCRIPTOR = _NUMBERSQUARED,
  __module__ = 'service_pb2'
  # @@protoc_insertion_point(class_scope:NumberSquared)
  ))
_sym_db.RegisterMessage(NumberSquared)



_SQUARESERVICE = _descriptor.ServiceDescriptor(
  name='SquareService',
  full_name='SquareService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=116,
  serialized_end=208,
  methods=[
  _descriptor.MethodDescriptor(
    name='SquareNumber',
    full_name='SquareService.SquareNumber',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_NUMBERSQUARED,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\r\022\013/v1/numbers')),
  ),
])
_sym_db.RegisterServiceDescriptor(_SQUARESERVICE)

DESCRIPTOR.services_by_name['SquareService'] = _SQUARESERVICE

# @@protoc_insertion_point(module_scope)