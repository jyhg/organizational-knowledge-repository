<script setup lang="ts">
import { ref } from 'vue'

const metrics = ref([
  { label: 'Faithfulness', value: 0.87, color: '#67C23A' },
  { label: 'Answer Relevancy', value: 0.82, color: '#409EFF' },
  { label: 'Context Precision', value: 0.79, color: '#E6A23C' },
  { label: 'Context Recall', value: 0.85, color: '#909399' },
])

const recentEvals = ref([
  { id: 1, name: '全量回归 #42', date: '2026-03-28', passed: 47, failed: 3, score: 0.94 },
  { id: 2, name: 'RAG 分块对比 #8', date: '2026-03-26', passed: 38, failed: 12, score: 0.76 },
  { id: 3, name: '安全测试 #15', date: '2026-03-25', passed: 22, failed: 5, score: 0.81 },
])
</script>

<template>
  <div class="eval-dashboard">
    <h3>评测指标概览</h3>
    <el-row :gutter="20" class="metrics-row">
      <el-col v-for="metric in metrics" :key="metric.label" :span="6">
        <el-card shadow="hover">
          <div class="metric-card">
            <span class="metric-label">{{ metric.label }}</span>
            <el-progress
              type="dashboard"
              :percentage="Math.round(metric.value * 100)"
              :color="metric.color"
              :width="100"
            />
          </div>
        </el-card>
      </el-col>
    </el-row>

    <h3>最近评测记录</h3>
    <el-table :data="recentEvals" stripe>
      <el-table-column prop="name" label="评测名称" />
      <el-table-column prop="date" label="日期" width="140" />
      <el-table-column prop="passed" label="通过" width="100">
        <template #default="{ row }">
          <el-tag type="success" size="small">{{ row.passed }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="failed" label="失败" width="100">
        <template #default="{ row }">
          <el-tag type="danger" size="small">{{ row.failed }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="总分" width="120">
        <template #default="{ row }">
          <el-progress :percentage="Math.round(row.score * 100)" :stroke-width="10" />
        </template>
      </el-table-column>
    </el-table>

    <div class="chart-placeholder">
      <el-empty description="ECharts 图表区域 — 待集成" />
    </div>
  </div>
</template>

<style scoped>
.eval-dashboard {
  padding: 16px;
}

.metrics-row {
  margin-bottom: 24px;
}

.metric-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}

.metric-label {
  font-weight: 600;
  font-size: 14px;
}

.chart-placeholder {
  margin-top: 24px;
  padding: 40px;
  border: 1px dashed var(--el-border-color);
  border-radius: 8px;
}
</style>
