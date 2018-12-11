# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game_packet.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import game_player_pb2 as game__player__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='game_packet.proto',
  package='',
  syntax='proto2',
  serialized_options=_b('\n\005protoB\017TcpPacketProtos'),
  serialized_pb=_b('\n\x11game_packet.proto\x1a\x11game_player.proto\"\xe7\x08\n\nGamePacket\x12$\n\x04type\x18\x01 \x02(\x0e\x32\x16.GamePacket.PacketType\x1a\xaa\x01\n\x10\x44isconnectPacket\x12$\n\x04type\x18\x01 \x02(\x0e\x32\x16.GamePacket.PacketType\x12\x1b\n\x06player\x18\x02 \x01(\x0b\x32\x0b.GamePlayer\x12\x33\n\x06update\x18\x03 \x01(\x0e\x32#.GamePacket.DisconnectPacket.Update\"\x1e\n\x06Update\x12\n\n\x06NORMAL\x10\x00\x12\x08\n\x04LOST\x10\x01\x1a\xc4\x01\n\rConnectPacket\x12$\n\x04type\x18\x01 \x02(\x0e\x32\x16.GamePacket.PacketType\x12\x1b\n\x06player\x18\x02 \x02(\x0b\x32\x0b.GamePlayer\x12\x10\n\x08lobby_id\x18\x03 \x01(\t\x12\x30\n\x06update\x18\x04 \x01(\x0e\x32 .GamePacket.ConnectPacket.Update\x12\x0f\n\x07\x61\x64\x64ress\x18\x05 \x02(\t\"\x1b\n\x06Update\x12\x08\n\x04SELF\x10\x00\x12\x07\n\x03NEW\x10\x01\x1a`\n\x11\x43reateLobbyPacket\x12$\n\x04type\x18\x01 \x02(\x0e\x32\x16.GamePacket.PacketType\x12\x10\n\x08lobby_id\x18\x02 \x01(\t\x12\x13\n\x0bmax_players\x18\x03 \x01(\x05\x1ak\n\nMovePacket\x12$\n\x04type\x18\x01 \x02(\x0e\x32\x16.GamePacket.PacketType\x12\x1b\n\x06player\x18\x02 \x02(\x0b\x32\x0b.GamePlayer\x12\x0c\n\x04newX\x18\x03 \x01(\x05\x12\x0c\n\x04newY\x18\x04 \x01(\x05\x1aZ\n\x10PlayerListPacket\x12$\n\x04type\x18\x01 \x02(\x0e\x32\x16.GamePacket.PacketType\x12 \n\x0bplayer_list\x18\x03 \x03(\x0b\x32\x0b.GamePlayer\x1a\x85\x01\n\tEndPacket\x12$\n\x04type\x18\x01 \x02(\x0e\x32\x16.GamePacket.PacketType\x12\x32\n\tcondition\x18\x02 \x02(\x0e\x32\x1f.GamePacket.EndPacket.Condition\"\x1e\n\tCondition\x12\x08\n\x04LOSE\x10\x00\x12\x07\n\x03WIN\x10\x01\x1aK\n\x0e\x45rrLfullPacket\x12$\n\x04type\x18\x01 \x02(\x0e\x32\x16.GamePacket.PacketType\x12\x13\n\x0b\x65rr_message\x18\x02 \x01(\t\x1a\x46\n\tErrPacket\x12$\n\x04type\x18\x01 \x02(\x0e\x32\x16.GamePacket.PacketType\x12\x13\n\x0b\x65rr_message\x18\x02 \x02(\t\"w\n\nPacketType\x12\x0e\n\nDISCONNECT\x10\x00\x12\x0b\n\x07\x43ONNECT\x10\x01\x12\x10\n\x0c\x43REATE_LOBBY\x10\x02\x12\x08\n\x04\x43HAT\x10\x03\x12\x0f\n\x0bPLAYER_LIST\x10\x04\x12\x07\n\x03\x45ND\x10\x05\x12\r\n\tERR_LFULL\x10\x06\x12\x07\n\x03\x45RR\x10\x07\x42\x18\n\x05protoB\x0fTcpPacketProtos')
  ,
  dependencies=[game__player__pb2.DESCRIPTOR,])



_GAMEPACKET_DISCONNECTPACKET_UPDATE = _descriptor.EnumDescriptor(
  name='Update',
  full_name='GamePacket.DisconnectPacket.Update',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOST', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=234,
  serialized_end=264,
)
_sym_db.RegisterEnumDescriptor(_GAMEPACKET_DISCONNECTPACKET_UPDATE)

_GAMEPACKET_CONNECTPACKET_UPDATE = _descriptor.EnumDescriptor(
  name='Update',
  full_name='GamePacket.ConnectPacket.Update',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SELF', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEW', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=436,
  serialized_end=463,
)
_sym_db.RegisterEnumDescriptor(_GAMEPACKET_CONNECTPACKET_UPDATE)

_GAMEPACKET_ENDPACKET_CONDITION = _descriptor.EnumDescriptor(
  name='Condition',
  full_name='GamePacket.EndPacket.Condition',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LOSE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WIN', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=868,
  serialized_end=898,
)
_sym_db.RegisterEnumDescriptor(_GAMEPACKET_ENDPACKET_CONDITION)

_GAMEPACKET_PACKETTYPE = _descriptor.EnumDescriptor(
  name='PacketType',
  full_name='GamePacket.PacketType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DISCONNECT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONNECT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATE_LOBBY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHAT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER_LIST', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERR_LFULL', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERR', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1049,
  serialized_end=1168,
)
_sym_db.RegisterEnumDescriptor(_GAMEPACKET_PACKETTYPE)


_GAMEPACKET_DISCONNECTPACKET = _descriptor.Descriptor(
  name='DisconnectPacket',
  full_name='GamePacket.DisconnectPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='GamePacket.DisconnectPacket.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player', full_name='GamePacket.DisconnectPacket.player', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='GamePacket.DisconnectPacket.update', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GAMEPACKET_DISCONNECTPACKET_UPDATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=264,
)

_GAMEPACKET_CONNECTPACKET = _descriptor.Descriptor(
  name='ConnectPacket',
  full_name='GamePacket.ConnectPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='GamePacket.ConnectPacket.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player', full_name='GamePacket.ConnectPacket.player', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lobby_id', full_name='GamePacket.ConnectPacket.lobby_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='GamePacket.ConnectPacket.update', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='GamePacket.ConnectPacket.address', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GAMEPACKET_CONNECTPACKET_UPDATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=267,
  serialized_end=463,
)

_GAMEPACKET_CREATELOBBYPACKET = _descriptor.Descriptor(
  name='CreateLobbyPacket',
  full_name='GamePacket.CreateLobbyPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='GamePacket.CreateLobbyPacket.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lobby_id', full_name='GamePacket.CreateLobbyPacket.lobby_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_players', full_name='GamePacket.CreateLobbyPacket.max_players', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=465,
  serialized_end=561,
)

_GAMEPACKET_MOVEPACKET = _descriptor.Descriptor(
  name='MovePacket',
  full_name='GamePacket.MovePacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='GamePacket.MovePacket.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player', full_name='GamePacket.MovePacket.player', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='newX', full_name='GamePacket.MovePacket.newX', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='newY', full_name='GamePacket.MovePacket.newY', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=563,
  serialized_end=670,
)

_GAMEPACKET_PLAYERLISTPACKET = _descriptor.Descriptor(
  name='PlayerListPacket',
  full_name='GamePacket.PlayerListPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='GamePacket.PlayerListPacket.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_list', full_name='GamePacket.PlayerListPacket.player_list', index=1,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=672,
  serialized_end=762,
)

_GAMEPACKET_ENDPACKET = _descriptor.Descriptor(
  name='EndPacket',
  full_name='GamePacket.EndPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='GamePacket.EndPacket.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='condition', full_name='GamePacket.EndPacket.condition', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GAMEPACKET_ENDPACKET_CONDITION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=765,
  serialized_end=898,
)

_GAMEPACKET_ERRLFULLPACKET = _descriptor.Descriptor(
  name='ErrLfullPacket',
  full_name='GamePacket.ErrLfullPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='GamePacket.ErrLfullPacket.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='err_message', full_name='GamePacket.ErrLfullPacket.err_message', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=900,
  serialized_end=975,
)

_GAMEPACKET_ERRPACKET = _descriptor.Descriptor(
  name='ErrPacket',
  full_name='GamePacket.ErrPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='GamePacket.ErrPacket.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='err_message', full_name='GamePacket.ErrPacket.err_message', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=977,
  serialized_end=1047,
)

_GAMEPACKET = _descriptor.Descriptor(
  name='GamePacket',
  full_name='GamePacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='GamePacket.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GAMEPACKET_DISCONNECTPACKET, _GAMEPACKET_CONNECTPACKET, _GAMEPACKET_CREATELOBBYPACKET, _GAMEPACKET_MOVEPACKET, _GAMEPACKET_PLAYERLISTPACKET, _GAMEPACKET_ENDPACKET, _GAMEPACKET_ERRLFULLPACKET, _GAMEPACKET_ERRPACKET, ],
  enum_types=[
    _GAMEPACKET_PACKETTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=1168,
)

_GAMEPACKET_DISCONNECTPACKET.fields_by_name['type'].enum_type = _GAMEPACKET_PACKETTYPE
_GAMEPACKET_DISCONNECTPACKET.fields_by_name['player'].message_type = game__player__pb2._GAMEPLAYER
_GAMEPACKET_DISCONNECTPACKET.fields_by_name['update'].enum_type = _GAMEPACKET_DISCONNECTPACKET_UPDATE
_GAMEPACKET_DISCONNECTPACKET.containing_type = _GAMEPACKET
_GAMEPACKET_DISCONNECTPACKET_UPDATE.containing_type = _GAMEPACKET_DISCONNECTPACKET
_GAMEPACKET_CONNECTPACKET.fields_by_name['type'].enum_type = _GAMEPACKET_PACKETTYPE
_GAMEPACKET_CONNECTPACKET.fields_by_name['player'].message_type = game__player__pb2._GAMEPLAYER
_GAMEPACKET_CONNECTPACKET.fields_by_name['update'].enum_type = _GAMEPACKET_CONNECTPACKET_UPDATE
_GAMEPACKET_CONNECTPACKET.containing_type = _GAMEPACKET
_GAMEPACKET_CONNECTPACKET_UPDATE.containing_type = _GAMEPACKET_CONNECTPACKET
_GAMEPACKET_CREATELOBBYPACKET.fields_by_name['type'].enum_type = _GAMEPACKET_PACKETTYPE
_GAMEPACKET_CREATELOBBYPACKET.containing_type = _GAMEPACKET
_GAMEPACKET_MOVEPACKET.fields_by_name['type'].enum_type = _GAMEPACKET_PACKETTYPE
_GAMEPACKET_MOVEPACKET.fields_by_name['player'].message_type = game__player__pb2._GAMEPLAYER
_GAMEPACKET_MOVEPACKET.containing_type = _GAMEPACKET
_GAMEPACKET_PLAYERLISTPACKET.fields_by_name['type'].enum_type = _GAMEPACKET_PACKETTYPE
_GAMEPACKET_PLAYERLISTPACKET.fields_by_name['player_list'].message_type = game__player__pb2._GAMEPLAYER
_GAMEPACKET_PLAYERLISTPACKET.containing_type = _GAMEPACKET
_GAMEPACKET_ENDPACKET.fields_by_name['type'].enum_type = _GAMEPACKET_PACKETTYPE
_GAMEPACKET_ENDPACKET.fields_by_name['condition'].enum_type = _GAMEPACKET_ENDPACKET_CONDITION
_GAMEPACKET_ENDPACKET.containing_type = _GAMEPACKET
_GAMEPACKET_ENDPACKET_CONDITION.containing_type = _GAMEPACKET_ENDPACKET
_GAMEPACKET_ERRLFULLPACKET.fields_by_name['type'].enum_type = _GAMEPACKET_PACKETTYPE
_GAMEPACKET_ERRLFULLPACKET.containing_type = _GAMEPACKET
_GAMEPACKET_ERRPACKET.fields_by_name['type'].enum_type = _GAMEPACKET_PACKETTYPE
_GAMEPACKET_ERRPACKET.containing_type = _GAMEPACKET
_GAMEPACKET.fields_by_name['type'].enum_type = _GAMEPACKET_PACKETTYPE
_GAMEPACKET_PACKETTYPE.containing_type = _GAMEPACKET
DESCRIPTOR.message_types_by_name['GamePacket'] = _GAMEPACKET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GamePacket = _reflection.GeneratedProtocolMessageType('GamePacket', (_message.Message,), dict(

  DisconnectPacket = _reflection.GeneratedProtocolMessageType('DisconnectPacket', (_message.Message,), dict(
    DESCRIPTOR = _GAMEPACKET_DISCONNECTPACKET,
    __module__ = 'game_packet_pb2'
    # @@protoc_insertion_point(class_scope:GamePacket.DisconnectPacket)
    ))
  ,

  ConnectPacket = _reflection.GeneratedProtocolMessageType('ConnectPacket', (_message.Message,), dict(
    DESCRIPTOR = _GAMEPACKET_CONNECTPACKET,
    __module__ = 'game_packet_pb2'
    # @@protoc_insertion_point(class_scope:GamePacket.ConnectPacket)
    ))
  ,

  CreateLobbyPacket = _reflection.GeneratedProtocolMessageType('CreateLobbyPacket', (_message.Message,), dict(
    DESCRIPTOR = _GAMEPACKET_CREATELOBBYPACKET,
    __module__ = 'game_packet_pb2'
    # @@protoc_insertion_point(class_scope:GamePacket.CreateLobbyPacket)
    ))
  ,

  MovePacket = _reflection.GeneratedProtocolMessageType('MovePacket', (_message.Message,), dict(
    DESCRIPTOR = _GAMEPACKET_MOVEPACKET,
    __module__ = 'game_packet_pb2'
    # @@protoc_insertion_point(class_scope:GamePacket.MovePacket)
    ))
  ,

  PlayerListPacket = _reflection.GeneratedProtocolMessageType('PlayerListPacket', (_message.Message,), dict(
    DESCRIPTOR = _GAMEPACKET_PLAYERLISTPACKET,
    __module__ = 'game_packet_pb2'
    # @@protoc_insertion_point(class_scope:GamePacket.PlayerListPacket)
    ))
  ,

  EndPacket = _reflection.GeneratedProtocolMessageType('EndPacket', (_message.Message,), dict(
    DESCRIPTOR = _GAMEPACKET_ENDPACKET,
    __module__ = 'game_packet_pb2'
    # @@protoc_insertion_point(class_scope:GamePacket.EndPacket)
    ))
  ,

  ErrLfullPacket = _reflection.GeneratedProtocolMessageType('ErrLfullPacket', (_message.Message,), dict(
    DESCRIPTOR = _GAMEPACKET_ERRLFULLPACKET,
    __module__ = 'game_packet_pb2'
    # @@protoc_insertion_point(class_scope:GamePacket.ErrLfullPacket)
    ))
  ,

  ErrPacket = _reflection.GeneratedProtocolMessageType('ErrPacket', (_message.Message,), dict(
    DESCRIPTOR = _GAMEPACKET_ERRPACKET,
    __module__ = 'game_packet_pb2'
    # @@protoc_insertion_point(class_scope:GamePacket.ErrPacket)
    ))
  ,
  DESCRIPTOR = _GAMEPACKET,
  __module__ = 'game_packet_pb2'
  # @@protoc_insertion_point(class_scope:GamePacket)
  ))
_sym_db.RegisterMessage(GamePacket)
_sym_db.RegisterMessage(GamePacket.DisconnectPacket)
_sym_db.RegisterMessage(GamePacket.ConnectPacket)
_sym_db.RegisterMessage(GamePacket.CreateLobbyPacket)
_sym_db.RegisterMessage(GamePacket.MovePacket)
_sym_db.RegisterMessage(GamePacket.PlayerListPacket)
_sym_db.RegisterMessage(GamePacket.EndPacket)
_sym_db.RegisterMessage(GamePacket.ErrLfullPacket)
_sym_db.RegisterMessage(GamePacket.ErrPacket)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)