// Code generated by protoc-gen-go. DO NOT EDIT.
// source: proto/v1/message.proto

package v1

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	_ "github.com/mwitkow/go-proto-validators"
	code "google.golang.org/genproto/googleapis/rpc/code"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type Response struct {
	Code                 code.Code `protobuf:"varint,1,opt,name=code,proto3,enum=google.rpc.Code" json:"code,omitempty"`
	Message              string    `protobuf:"bytes,2,opt,name=message,proto3" json:"message,omitempty"`
	XXX_NoUnkeyedLiteral struct{}  `json:"-"`
	XXX_unrecognized     []byte    `json:"-"`
	XXX_sizecache        int32     `json:"-"`
}

func (m *Response) Reset()         { *m = Response{} }
func (m *Response) String() string { return proto.CompactTextString(m) }
func (*Response) ProtoMessage()    {}
func (*Response) Descriptor() ([]byte, []int) {
	return fileDescriptor_9f8f48ac3db94d51, []int{0}
}

func (m *Response) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Response.Unmarshal(m, b)
}
func (m *Response) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Response.Marshal(b, m, deterministic)
}
func (m *Response) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Response.Merge(m, src)
}
func (m *Response) XXX_Size() int {
	return xxx_messageInfo_Response.Size(m)
}
func (m *Response) XXX_DiscardUnknown() {
	xxx_messageInfo_Response.DiscardUnknown(m)
}

var xxx_messageInfo_Response proto.InternalMessageInfo

func (m *Response) GetCode() code.Code {
	if m != nil {
		return m.Code
	}
	return code.Code_OK
}

func (m *Response) GetMessage() string {
	if m != nil {
		return m.Message
	}
	return ""
}

func init() {
	proto.RegisterType((*Response)(nil), "proto.v1.Response")
}

func init() { proto.RegisterFile("proto/v1/message.proto", fileDescriptor_9f8f48ac3db94d51) }

var fileDescriptor_9f8f48ac3db94d51 = []byte{
	// 191 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xe2, 0x12, 0x2b, 0x28, 0xca, 0x2f,
	0xc9, 0xd7, 0x2f, 0x33, 0xd4, 0xcf, 0x4d, 0x2d, 0x2e, 0x4e, 0x4c, 0x4f, 0xd5, 0x03, 0x0b, 0x08,
	0x71, 0x80, 0x29, 0xbd, 0x32, 0x43, 0x29, 0xb3, 0xf4, 0xcc, 0x92, 0x8c, 0xd2, 0x24, 0xbd, 0xe4,
	0xfc, 0x5c, 0xfd, 0xdc, 0xf2, 0xcc, 0x92, 0xec, 0xfc, 0x72, 0xfd, 0xf4, 0x7c, 0x5d, 0xb0, 0xbc,
	0x6e, 0x59, 0x62, 0x4e, 0x66, 0x4a, 0x62, 0x49, 0x7e, 0x51, 0xb1, 0x3e, 0x9c, 0x09, 0x31, 0x41,
	0x4a, 0x34, 0x3d, 0x3f, 0x3f, 0x3d, 0x27, 0x55, 0xbf, 0xa8, 0x20, 0x59, 0x3f, 0x39, 0x3f, 0x05,
	0x6a, 0xb0, 0x52, 0x30, 0x17, 0x47, 0x50, 0x6a, 0x71, 0x41, 0x7e, 0x5e, 0x71, 0xaa, 0x90, 0x2e,
	0x17, 0x0b, 0x48, 0x46, 0x82, 0x51, 0x81, 0x51, 0x83, 0xcf, 0x48, 0x40, 0x0f, 0xa2, 0x43, 0xaf,
	0xa8, 0x20, 0x59, 0xcf, 0x39, 0x3f, 0x25, 0xd5, 0x89, 0xfd, 0xd1, 0x7d, 0x79, 0xe6, 0x0e, 0x46,
	0xc6, 0x20, 0xb0, 0x32, 0x21, 0x09, 0x2e, 0x76, 0xa8, 0x23, 0x25, 0x98, 0x14, 0x18, 0x35, 0x38,
	0x83, 0x60, 0x5c, 0x27, 0xde, 0x28, 0xee, 0x82, 0x24, 0x7d, 0x98, 0x57, 0x92, 0xd8, 0xc0, 0x2c,
	0x63, 0x40, 0x00, 0x00, 0x00, 0xff, 0xff, 0x71, 0xf7, 0x82, 0x01, 0xdd, 0x00, 0x00, 0x00,
}