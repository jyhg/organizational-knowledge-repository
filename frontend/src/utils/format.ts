export function formatTimestamp(ts: number): string {
  return new Date(ts).toLocaleString('zh-CN')
}

export function truncate(text: string, maxLength: number = 100): string {
  if (text.length <= maxLength) return text
  return text.slice(0, maxLength) + '...'
}
