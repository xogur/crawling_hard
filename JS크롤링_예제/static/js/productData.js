const productData = {
    "items": [
        { "id": 101, "name": "Laptop", "price": 1000 },
        { "id": 102, "name": "Smartphone", "price": 400 },
        { "id": 103, "name": "Tablet", "price": 200 }
    ],
    "itemCnt": 3,
    "category": 12
};

var productList = document.getElementById("product_list"); // ul 요소 가져오기

// productData 객체의 items 배열 순회
productData.items.forEach(function (item) {
    var li = document.createElement("li"); // li 생성
    li.textContent = "제품명: " + item.name + ", 가격: " + item.price + "원"; // 텍스트 설정
    productList.appendChild(li); // ul에 li 추가
});