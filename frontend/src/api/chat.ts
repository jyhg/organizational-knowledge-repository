import apiClient from './client'

export interface ChatRequest {
  message: string
  conversation_id?: string
}

export interface ChatResponse {
  answer: string
  sources: string[]
  conversation_id: string
}

export function sendChatMessage(data: ChatRequest) {
  return apiClient.post<ChatResponse>('/chat', data)
}
