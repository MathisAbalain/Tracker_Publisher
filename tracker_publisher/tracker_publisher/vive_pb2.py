# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/vive.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/vive.proto',
  package='vive_provider',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x10proto/vive.proto\x12\rvive_provider\"+\n\x08Vector3d\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02\x12\t\n\x01z\x18\x03 \x02(\x02\"<\n\nQuaternion\x12\n\n\x02qw\x18\x01 \x02(\x02\x12\n\n\x02qx\x18\x02 \x02(\x02\x12\n\n\x02qy\x18\x03 \x02(\x02\x12\n\n\x02qz\x18\x04 \x02(\x02\"\xb3\x01\n\tMatrix4x3\x12\x0c\n\x04i0j0\x18\x01 \x02(\x02\x12\x0c\n\x04i0j1\x18\x02 \x02(\x02\x12\x0c\n\x04i0j2\x18\x03 \x02(\x02\x12\x0c\n\x04i0j3\x18\x04 \x02(\x02\x12\x0c\n\x04i1j0\x18\x05 \x02(\x02\x12\x0c\n\x04i1j1\x18\x06 \x02(\x02\x12\x0c\n\x04i1j2\x18\x07 \x02(\x02\x12\x0c\n\x04i1j3\x18\x08 \x02(\x02\x12\x0c\n\x04i2j0\x18\t \x02(\x02\x12\x0c\n\x04i2j1\x18\n \x02(\x02\x12\x0c\n\x04i2j2\x18\x0b \x02(\x02\x12\x0c\n\x04i2j3\x18\x0c \x02(\x02\"\xf9\x01\n\nTrackerMsg\x12\x13\n\x0btracker_idx\x18\x01 \x02(\r\x12\x1f\n\x17time_since_last_tracked\x18\x02 \x01(\x04\x12$\n\x03pos\x18\x03 \x01(\x0b\x32\x17.vive_provider.Vector3d\x12.\n\x0borientation\x18\x04 \x01(\x0b\x32\x19.vive_provider.Quaternion\x12\x33\n\x12\x63\x61rtesian_velocity\x18\x05 \x01(\x0b\x32\x17.vive_provider.Vector3d\x12\x15\n\rserial_number\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65vice_type\x18\x08 \x01(\t\"\xaa\x01\n\tGlobalMsg\x12\x16\n\x0evive_timestamp\x18\x01 \x01(\x04\x12\x18\n\x10time_since_epoch\x18\x02 \x01(\x04\x12+\n\x08trackers\x18\x03 \x03(\x0b\x32\x19.vive_provider.TrackerMsg\x12\x0b\n\x03seq\x18\x04 \x01(\x04\x12\x31\n\x10tagged_positions\x18\x05 \x03(\x0b\x32\x17.vive_provider.Vector3d\"q\n\x10GlobalCollection\x12*\n\x08messages\x18\x01 \x03(\x0b\x32\x18.vive_provider.GlobalMsg\x12\x31\n\x10tagged_positions\x18\x02 \x03(\x0b\x32\x17.vive_provider.Vector3d')
)




_VECTOR3D = _descriptor.Descriptor(
  name='Vector3d',
  full_name='vive_provider.Vector3d',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='vive_provider.Vector3d.x', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='vive_provider.Vector3d.y', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='vive_provider.Vector3d.z', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=78,
)


_QUATERNION = _descriptor.Descriptor(
  name='Quaternion',
  full_name='vive_provider.Quaternion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='qw', full_name='vive_provider.Quaternion.qw', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qx', full_name='vive_provider.Quaternion.qx', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qy', full_name='vive_provider.Quaternion.qy', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qz', full_name='vive_provider.Quaternion.qz', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=140,
)


_MATRIX4X3 = _descriptor.Descriptor(
  name='Matrix4x3',
  full_name='vive_provider.Matrix4x3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='i0j0', full_name='vive_provider.Matrix4x3.i0j0', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i0j1', full_name='vive_provider.Matrix4x3.i0j1', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i0j2', full_name='vive_provider.Matrix4x3.i0j2', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i0j3', full_name='vive_provider.Matrix4x3.i0j3', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i1j0', full_name='vive_provider.Matrix4x3.i1j0', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i1j1', full_name='vive_provider.Matrix4x3.i1j1', index=5,
      number=6, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i1j2', full_name='vive_provider.Matrix4x3.i1j2', index=6,
      number=7, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i1j3', full_name='vive_provider.Matrix4x3.i1j3', index=7,
      number=8, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i2j0', full_name='vive_provider.Matrix4x3.i2j0', index=8,
      number=9, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i2j1', full_name='vive_provider.Matrix4x3.i2j1', index=9,
      number=10, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i2j2', full_name='vive_provider.Matrix4x3.i2j2', index=10,
      number=11, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i2j3', full_name='vive_provider.Matrix4x3.i2j3', index=11,
      number=12, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=322,
)


_TRACKERMSG = _descriptor.Descriptor(
  name='TrackerMsg',
  full_name='vive_provider.TrackerMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tracker_idx', full_name='vive_provider.TrackerMsg.tracker_idx', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_since_last_tracked', full_name='vive_provider.TrackerMsg.time_since_last_tracked', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pos', full_name='vive_provider.TrackerMsg.pos', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='vive_provider.TrackerMsg.orientation', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cartesian_velocity', full_name='vive_provider.TrackerMsg.cartesian_velocity', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serial_number', full_name='vive_provider.TrackerMsg.serial_number', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_type', full_name='vive_provider.TrackerMsg.device_type', index=6,
      number=8, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=325,
  serialized_end=574,
)


_GLOBALMSG = _descriptor.Descriptor(
  name='GlobalMsg',
  full_name='vive_provider.GlobalMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vive_timestamp', full_name='vive_provider.GlobalMsg.vive_timestamp', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_since_epoch', full_name='vive_provider.GlobalMsg.time_since_epoch', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trackers', full_name='vive_provider.GlobalMsg.trackers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seq', full_name='vive_provider.GlobalMsg.seq', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagged_positions', full_name='vive_provider.GlobalMsg.tagged_positions', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=577,
  serialized_end=747,
)


_GLOBALCOLLECTION = _descriptor.Descriptor(
  name='GlobalCollection',
  full_name='vive_provider.GlobalCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messages', full_name='vive_provider.GlobalCollection.messages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tagged_positions', full_name='vive_provider.GlobalCollection.tagged_positions', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=749,
  serialized_end=862,
)

_TRACKERMSG.fields_by_name['pos'].message_type = _VECTOR3D
_TRACKERMSG.fields_by_name['orientation'].message_type = _QUATERNION
_TRACKERMSG.fields_by_name['cartesian_velocity'].message_type = _VECTOR3D
_GLOBALMSG.fields_by_name['trackers'].message_type = _TRACKERMSG
_GLOBALMSG.fields_by_name['tagged_positions'].message_type = _VECTOR3D
_GLOBALCOLLECTION.fields_by_name['messages'].message_type = _GLOBALMSG
_GLOBALCOLLECTION.fields_by_name['tagged_positions'].message_type = _VECTOR3D
DESCRIPTOR.message_types_by_name['Vector3d'] = _VECTOR3D
DESCRIPTOR.message_types_by_name['Quaternion'] = _QUATERNION
DESCRIPTOR.message_types_by_name['Matrix4x3'] = _MATRIX4X3
DESCRIPTOR.message_types_by_name['TrackerMsg'] = _TRACKERMSG
DESCRIPTOR.message_types_by_name['GlobalMsg'] = _GLOBALMSG
DESCRIPTOR.message_types_by_name['GlobalCollection'] = _GLOBALCOLLECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Vector3d = _reflection.GeneratedProtocolMessageType('Vector3d', (_message.Message,), dict(
  DESCRIPTOR = _VECTOR3D,
  __module__ = 'proto.vive_pb2'
  # @@protoc_insertion_point(class_scope:vive_provider.Vector3d)
  ))
_sym_db.RegisterMessage(Vector3d)

Quaternion = _reflection.GeneratedProtocolMessageType('Quaternion', (_message.Message,), dict(
  DESCRIPTOR = _QUATERNION,
  __module__ = 'proto.vive_pb2'
  # @@protoc_insertion_point(class_scope:vive_provider.Quaternion)
  ))
_sym_db.RegisterMessage(Quaternion)

Matrix4x3 = _reflection.GeneratedProtocolMessageType('Matrix4x3', (_message.Message,), dict(
  DESCRIPTOR = _MATRIX4X3,
  __module__ = 'proto.vive_pb2'
  # @@protoc_insertion_point(class_scope:vive_provider.Matrix4x3)
  ))
_sym_db.RegisterMessage(Matrix4x3)

TrackerMsg = _reflection.GeneratedProtocolMessageType('TrackerMsg', (_message.Message,), dict(
  DESCRIPTOR = _TRACKERMSG,
  __module__ = 'proto.vive_pb2'
  # @@protoc_insertion_point(class_scope:vive_provider.TrackerMsg)
  ))
_sym_db.RegisterMessage(TrackerMsg)

GlobalMsg = _reflection.GeneratedProtocolMessageType('GlobalMsg', (_message.Message,), dict(
  DESCRIPTOR = _GLOBALMSG,
  __module__ = 'proto.vive_pb2'
  # @@protoc_insertion_point(class_scope:vive_provider.GlobalMsg)
  ))
_sym_db.RegisterMessage(GlobalMsg)

GlobalCollection = _reflection.GeneratedProtocolMessageType('GlobalCollection', (_message.Message,), dict(
  DESCRIPTOR = _GLOBALCOLLECTION,
  __module__ = 'proto.vive_pb2'
  # @@protoc_insertion_point(class_scope:vive_provider.GlobalCollection)
  ))
_sym_db.RegisterMessage(GlobalCollection)


# @@protoc_insertion_point(module_scope)