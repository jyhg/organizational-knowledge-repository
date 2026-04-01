<script setup lang="ts">
import { ref } from 'vue'
import { Upload, Search } from '@element-plus/icons-vue'

interface KnowledgeDoc {
  id: string
  title: string
  category: string
  updatedAt: string
  status: 'indexed' | 'pending' | 'failed'
}

const searchQuery = ref('')
const documents = ref<KnowledgeDoc[]>([
  { id: '1', title: '供应商准入标准 v2.1', category: '采购管理', updatedAt: '2026-03-28', status: 'indexed' },
  { id: '2', title: '入库操作SOP', category: '仓储物流', updatedAt: '2026-03-25', status: 'indexed' },
  { id: '3', title: '退换货政策 2026版', category: '订单履约', updatedAt: '2026-03-20', status: 'pending' },
])

const statusTagType: Record<string, string> = {
  indexed: 'success',
  pending: 'warning',
  failed: 'danger',
}

const statusLabel: Record<string, string> = {
  indexed: '已索引',
  pending: '处理中',
  failed: '失败',
}
</script>

<template>
  <div class="docs-manage">
    <div class="toolbar">
      <el-input v-model="searchQuery" :prefix-icon="Search" placeholder="搜索文档..." style="width: 300px" />
      <el-button type="primary" :icon="Upload">上传文档</el-button>
    </div>

    <el-table :data="documents" stripe style="width: 100%">
      <el-table-column prop="title" label="文档标题" />
      <el-table-column prop="category" label="分类" width="150" />
      <el-table-column prop="updatedAt" label="更新时间" width="150" />
      <el-table-column label="状态" width="120">
        <template #default="{ row }">
          <el-tag :type="statusTagType[row.status]" size="small">
            {{ statusLabel[row.status] }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="180">
        <template #default>
          <el-button size="small" type="primary" text>编辑</el-button>
          <el-button size="small" type="info" text>重新索引</el-button>
          <el-button size="small" type="danger" text>删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<style scoped>
.docs-manage {
  padding: 16px;
}

.toolbar {
  display: flex;
  justify-content: space-between;
  margin-bottom: 16px;
}
</style>
