import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import { createRouter, createMemoryHistory } from 'vue-router'
import AppLayout from '../AppLayout.vue'

const router = createRouter({
  history: createMemoryHistory(),
  routes: [{ path: '/', component: { template: '<div />' } }],
})

describe('AppLayout', () => {
  it('renders the title', () => {
    const wrapper = mount(AppLayout, {
      global: { plugins: [router] },
    })
    expect(wrapper.text()).toContain('供应链知识库')
  })
})
