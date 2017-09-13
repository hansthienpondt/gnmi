# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from testing.fake.proto import fake_pb2 as testing_dot_fake_dot_proto_dot_fake__pb2


class AgentManagerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Add = channel.unary_unary(
        '/gnmi.fake.AgentManager/Add',
        request_serializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.SerializeToString,
        response_deserializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.FromString,
        )
    self.Remove = channel.unary_unary(
        '/gnmi.fake.AgentManager/Remove',
        request_serializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.SerializeToString,
        response_deserializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.FromString,
        )
    self.Get = channel.unary_unary(
        '/gnmi.fake.AgentManager/Get',
        request_serializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.SerializeToString,
        response_deserializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.FromString,
        )


class AgentManagerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Add(self, request, context):
    """Add adds an agent to the server.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Remove(self, request, context):
    """Remove removes an agent from the server.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get(self, request, context):
    """Get returns the current status of an agent on the server.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AgentManagerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Add': grpc.unary_unary_rpc_method_handler(
          servicer.Add,
          request_deserializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.FromString,
          response_serializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.SerializeToString,
      ),
      'Remove': grpc.unary_unary_rpc_method_handler(
          servicer.Remove,
          request_deserializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.FromString,
          response_serializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.FromString,
          response_serializer=testing_dot_fake_dot_proto_dot_fake__pb2.Config.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'gnmi.fake.AgentManager', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))