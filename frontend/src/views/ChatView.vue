<script setup lang="ts">
import { ref } from 'vue'
import { Promotion } from '@element-plus/icons-vue'
import { sendChatMessage } from '@/api/chat'

interface Message {
  role: 'user' | 'assistant'
  content: string
  sources?: string[]
}

const inputMessage = ref('')
const messages = ref<Message[]>([
  {
    role: 'assistant',
    content: '你好！我是供应链知识库助手，可以回答关于采购、仓储、物流、订单履约等方面的问题。请问有什么可以帮你的？',
  },
])
const loading = ref(false)
const conversationId = ref<string | undefined>(undefined)

async function sendMessage() {
  const content = inputMessage.value.trim()
  if (!content || loading.value) return

  messages.value.push({ role: 'user', content })
  inputMessage.value = ''
  loading.value = true

  try {
    const res = await sendChatMessage({ message: content, conversation_id: conversationId.value })
    conversationId.value = res.data.conversation_id
    messages.value.push({
      role: 'assistant',
      content: res.data.answer,
      sources: res.data.sources,
    })
  } catch (err) {
    messages.value.push({
      role: 'assistant',
      content: '请求失败，请检查后端服务是否正常运行。',
      sources: [],
    })
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="chat-container">
    <div class="message-list">
      <div
        v-for="(msg, index) in messages"
        :key="index"
        :class="['message', msg.role]"
      >
        <el-avatar :size="32">
          {{ msg.role === 'user' ? 'U' : 'AI' }}
        </el-avatar>
        <div class="message-content">
          <p>{{ msg.content }}</p>
          <div v-if="msg.sources?.length" class="sources">
            <el-tag v-for="src in msg.sources" :key="src" size="small" type="info">
              {{ src }}
            </el-tag>
          </div>
        </div>
      </div>
      <div v-if="loading" class="message assistant">
        <el-avatar :size="32">AI</el-avatar>
        <div class="message-content">
          <el-skeleton :rows="2" animated />
        </div>
      </div>
    </div>

    <div class="input-area">
      <el-input
        v-model="inputMessage"
        placeholder="输入你的问题..."
        :rows="2"
        type="textarea"
        resize="none"
        @keydown.enter.exact.prevent="sendMessage"
      />
      <el-button
        type="primary"
        :icon="Promotion"
        :loading="loading"
        @click="sendMessage"
      >
        发送
      </el-button>
    </div>
  </div>
</template>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height: calc(100vh - 120px);
}

.message-list {
  flex: 1;
  overflow-y: auto;
  padding: 16px;
}

.message {
  display: flex;
  gap: 12px;
  margin-bottom: 16px;
}

.message.user {
  flex-direction: row-reverse;
}

.message-content {
  max-width: 70%;
  padding: 12px 16px;
  border-radius: 8px;
  background: var(--el-fill-color-light);
}

.message.user .message-content {
  background: var(--el-color-primary-light-9);
}

.sources {
  margin-top: 8px;
  display: flex;
  gap: 4px;
  flex-wrap: wrap;
}

.input-area {
  display: flex;
  gap: 12px;
  padding: 16px;
  border-top: 1px solid var(--el-border-color);
  align-items: flex-end;
}

.input-area .el-input {
  flex: 1;
}
</style>
