function findMarkdownFiles(dirs, ignore) {
    let markdownFiles = []
  
    function traverseDirectory(dir, ignore) {
      const files = fs.readdirSync(dir)
      if (ignore.includes(dir)) {
        return
      }
  
      files.forEach((file) => {
        const filePath = path.join(dir, file)
        const stats = fs.statSync(filePath, ignore)
  
        if (stats.isDirectory()) {
          traverseDirectory(filePath, ignore)
        } else if (path.extname(file) === '.md') {
          const content = fs.readFileSync(filePath, 'utf8')
          const markdownFile = {
            text: content,
            filename: file,
            path: filePath,
          }
          markdownFiles.push(markdownFile)
        }
      })
    }
  
    dirs.forEach((dir) => {
      traverseDirectory(dir, ignore)
    })
  
    return markdownFiles
  }