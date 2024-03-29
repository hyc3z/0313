import 'package:flutter/cupertino.dart';
import 'package:conge_ai_chatgpt/services/message_service.dart';

import '../models/chat_model.dart';
import '../services/api_service.dart';

class ChatProvider with ChangeNotifier {
  List<ChatModel> chatList = [];
  List<ChatModel> get getChatList {
    return chatList;
  }

  void addUserMessage({required String msg}) {
    chatList.add(ChatModel(msg: msg, chatIndex: 0));
    notifyListeners();
  }

  void updateMessageStatus({required int currentIndex}) {
    chatList[currentIndex].isAnimated = true;
    notifyListeners();
  }

  Future<void> sendMessageAndGetAnswers(
      {required String msg, required String chosenModelId}) async {
    if (chosenModelId.toLowerCase().startsWith("gpt")) {
      chatList.addAll(await ApiService.sendMessageGPT(
        message: MessageService.getMessage(chatList),
        modelId: chosenModelId,
      ));
    } else {
      chatList.addAll(await ApiService.sendMessage(
        message: MessageService.getMessage(chatList),
        modelId: chosenModelId,
      ));
    }
    notifyListeners();
  }
}
