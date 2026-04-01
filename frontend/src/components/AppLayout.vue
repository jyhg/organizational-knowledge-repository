<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { ChatDotRound, Document, DataAnalysis } from '@element-plus/icons-vue'

const router = useRouter()
const isCollapse = ref(false)

const menuItems = [
  { index: '/chat', title: '知识问答', icon: ChatDotRound },
  { index: '/docs', title: '知识管理', icon: Document },
  { index: '/eval', title: '评测看板', icon: DataAnalysis },
]

function handleMenuSelect(index: string) {
  router.push(index)
}
</script>

<template>
  <el-container class="app-container">
    <el-aside :width="isCollapse ? '64px' : '200px'">
      <div class="logo-area">
        <h2 v-if="!isCollapse">供应链知识库</h2>
        <span v-else>KB</span>
      </div>
      <el-menu
        default-active="/chat"
        :collapse="isCollapse"
        :router="false"
        @select="handleMenuSelect"
      >
        <el-menu-item v-for="item in menuItems" :key="item.index" :index="item.index">
          <el-icon><component :is="item.icon" /></el-icon>
          <template #title>{{ item.title }}</template>
        </el-menu-item>
      </el-menu>
    </el-aside>

    <el-container>
      <el-header>
        <el-button :icon="isCollapse ? 'Expand' : 'Fold'" text @click="isCollapse = !isCollapse" />
        <span class="header-title">企业级AI电商供应链知识库</span>
      </el-header>

      <el-main>
        <slot />
      </el-main>
    </el-container>
  </el-container>
</template>

<style scoped>
.app-container {
  height: 100vh;
}

.logo-area {
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-bottom: 1px solid var(--el-border-color);
}

.logo-area h2 {
  font-size: 16px;
  margin: 0;
}

.el-aside {
  border-right: 1px solid var(--el-border-color);
  transition: width 0.3s;
}

.el-header {
  display: flex;
  align-items: center;
  border-bottom: 1px solid var(--el-border-color);
}

.header-title {
  margin-left: 12px;
  font-size: 16px;
  font-weight: 600;
}
</style>
