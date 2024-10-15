function createNavigationButton(direction) {
  const button = document.createElement('div');
  button.className = `pdf-nav-button ${direction}-button`;
  button.textContent = direction === 'prev' ? '←' : '→';
  button.addEventListener('click', () => navigatePDF(direction));
  return button;
}

function navigatePDF(direction) {
  const url = new URL(window.location.href);
  const path = url.pathname;
  const match = path.match(/(\d+)_(\d+)\.txt$/);

  if (match) {
    let currentChapter = parseInt(match[1]);
    let currentSection = parseInt(match[2]);

    const checkFile = (chapter, section) => {
      const newPath = path.replace(/\d+_\d+\.txt$/, `${chapter}_${section}.txt`);
      fetch(newPath, { method: 'HEAD' })
        .then(response => {
          if (response.ok) {
            console.log(`檔案 ${newPath} 存在，導航到該檔案`);
            window.location.href = url.origin + newPath;
          } else if (response.status === 404) {
            console.log(`檔案 ${newPath} 不存在`);
            if (direction === 'next') {
              if (section === 1) {
                alert('已經是最後一個檔案');
              } else {
                checkFile(chapter + 1, 1);
              }
            } else {
              if (section === 1) {
                findLastSection(chapter - 1);
              } else {
                checkFile(chapter, section - 1);
              }
            }
          } else {
            console.log(`檔案 ${newPath} 無法訪問，停止尋找`);
            alert('檔案無法訪問，停止尋找');
          }
        })
        .catch(() => {
          alert('發生錯誤，無法尋找檔案');
        });
    };

    const findLastSection = (chapter) => {
      let section = 1;
      const checkNextSection = () => {
        const newPath = path.replace(/\d+_\d+\.txt$/, `${chapter}_${section}.txt`);
        fetch(newPath, { method: 'HEAD' })
          .then(response => {
            if (response.ok) {
              section++;
              checkNextSection();
            } else {
              if (section > 1) {
                window.location.href = url.origin + path.replace(/\d+_\d+\.txt$/, `${chapter}_${section - 1}.txt`);
              } else {
                alert('找不到上一章的檔案');
              }
            }
          })
          .catch(() => {
            alert('發生錯誤，無法尋找檔案');
          });
      };
      checkNextSection();
    };

    if (direction === 'next') {
      checkFile(currentChapter, currentSection + 1);
    } else {
      if (currentSection === 1) {
        findLastSection(currentChapter - 1);
      } else {
        checkFile(currentChapter, currentSection - 1);
      }
    }
  }
}

function init() {
  const body = document.body;

  const prevButton = createNavigationButton('prev');
  const nextButton = createNavigationButton('next');

  body.appendChild(prevButton);
  body.appendChild(nextButton);
}

// 等待 DOM 完全加載后再初始化
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}

// 添加錯誤處理和日誌記錄
window.addEventListener('error', function (event) {
  console.error('捕獲到全局錯誤:', event.error);
});

console.log('content.js 已加載');