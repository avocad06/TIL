```javascript
const fetchTours = async () => {
    setLoading(true);
    const response = await fetch(url);
    const tours = await response.json();
}
```

`fetchTours` 함수는 비동기로 data를 fetch 받아와서 json으로 파싱하는 함수



- 통신 에러 핸들링 : `try-catch`문 활용

  ```javascript
  const fetchTours = async () => {
      setLoading(true);
      
      try {
      const response = await fetch(url);
      const tours = await response.json();
          setLoading(false);
          setTours(tours);
      } catch(error) {
          setLoading(false;)
          console.log(error)
      }
  
  }
  ```

  

- Tour 아이템 `/Tour.js`

  ```jsx
  <article>
      <img/>
      <footer>
          <div 'tour-info'>
              <h4>{name}</h4>
              <h4 'tour-price'></h4>
          </div>
          <p>{info}</p>
          <button 'delete-btn'>not interested</button>
      </footer>
  </article>
  ```



- 설명 디테일 toggle

  > conditional rendering

  ```jsx
  <p>{readMore ? info : `${info.substring(0, 200)}`}...
  <button onClick={() => setReadMore(!readMore)>
              {readMore ? '접기' : '더보기'}</button>
  </p>
  ```
  
  

