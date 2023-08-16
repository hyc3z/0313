import 'dart:convert';
import 'dart:developer';
import 'dart:io';

import 'package:conge_ai_chatgpt/constants/api_consts.dart';
import 'package:conge_ai_chatgpt/models/chat_model.dart';
import 'package:conge_ai_chatgpt/models/models_model.dart';
import 'package:http/http.dart' as http;

class AzureFunctionChatModelV1 {
  String sender;
  String text;

  AzureFunctionChatModelV1({required this.sender, required this.text});

  Map<String, dynamic> toJson() => {
    'sender': sender,
    'text': text,
  };
}
class MessageService {
  static String getMessage(List<ChatModel> chatList) {
    List<AzureFunctionChatModelV1> result = <AzureFunctionChatModelV1>[];
    for (var i = 0; i < chatList.length; i++) {
      var currentMessage = AzureFunctionChatModelV1(sender: chatList[i].chatIndex == 0 ? "user" : "system", text: chatList[i].msg.trim());
      result.add(currentMessage);
    }
    return jsonEncode(result);
  }
}
