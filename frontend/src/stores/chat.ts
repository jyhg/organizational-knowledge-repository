import { ref } from 'vue'
import { defineStore } from 'pinia'

export interface Message {
  role: 'user' | 'assistant'
  content: string
  sources?: string[]
  timestamp: number
}

export const useChatStore = defineStore('chat', () => {
  const messages = ref<Message[]>([])
  const loading = ref(false)

  function addMessage(msg: Omit<Message, 'timestamp'>) {
    messages.value.push({ ...msg, timestamp: Date.now() })
  }

  function clearMessages() {
    messages.value = []
  }

  return { messages, loading, addMessage, clearMessages }
})
