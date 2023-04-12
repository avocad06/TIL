let timer;
const inputForm = document.querySelector('#input')
inputForm.addEventListener('input', () => {
    console.log("api 요청 보내기 전 입력")
    // if (timer) clearTimeout(timer);
    timer = setTimeout(() => {
        alert("1초 후 api 요청")
    }, 1000);
})


/*
document.querySelector('#input').addEventListener('input', () => {
    console.log(timer)
    if (!timer) {
        timer = setTimeout(() => {
            timer = null;
            console.log("쓰로틀링 API 요청")
        }, 400)
    }
})
*/