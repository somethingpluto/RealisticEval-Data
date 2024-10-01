/**
 * NOTE: this function created by ChatGPT
 */
export const mapString = (keyString: string) => {
    if (!ENCRYPT.enable) return keyString
    if (keyString.length === 64) return keyString
    if (keyString.length > 64) {
      throw new Error('keyString length must less than 64')
    }
  
    if (!keyString) {
      throw new Error('keyString must not be empty')
    }
  
    const hash = crypto.createHash('sha256')
    hash.update(keyString + SALT)
    const digest = hash.digest('hex')
    if (digest.length >= 64) {
      return digest.slice(0, 64) // 如果哈希值的长度大于等于 64，直接返回哈希值
    } else {
      const padding = '0'.repeat(64 - digest.length) // 使用 0 填充到 64 位
      return padding + digest
    }
  }