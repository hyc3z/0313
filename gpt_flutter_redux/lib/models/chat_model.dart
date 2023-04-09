class ChatModel {
  final String msg;
  final int chatIndex;
  int currentIndex = 0;
  bool isAnimated;
  static int currentChatIndex = 0;

  ChatModel({required this.msg, required this.chatIndex, this.isAnimated = false}) {
    currentIndex = currentChatIndex++;
  }

  factory ChatModel.fromJson(Map<String, dynamic> json) => ChatModel(
    msg: json["msg"],
    chatIndex: json["chatIndex"],
  );
}
