class ChatModel {
  final String msg;
  final int chatIndex;
  bool isAnimated;

  ChatModel({required this.msg, required this.chatIndex, this.isAnimated = false});

  factory ChatModel.fromJson(Map<String, dynamic> json) => ChatModel(
        msg: json["msg"],
        chatIndex: json["chatIndex"],
      );
}
