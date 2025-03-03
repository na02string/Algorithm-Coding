# [level 2] N-Queen - 12952 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12952) 

### 성능 요약

메모리: 10.3 MB, 시간: 9869.33 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2025년 03월 03일 16:48:13

### 문제 설명

<p>가로, 세로 길이가 n인 정사각형으로된 체스판이 있습니다. 체스판 위의 n개의 퀸이 서로를 공격할 수 없도록 배치하고 싶습니다.</p>

<p>예를 들어서 n이 4인경우 다음과 같이 퀸을 배치하면 n개의 퀸은 서로를 한번에 공격 할 수 없습니다.</p>

<p><img src="https://i.imgur.com/lt2zdK6.png" title="" alt="Imgur"><br>
<img src="https://i.imgur.com/5c5EUrq.png" title="" alt="Imgur"></p>

<p>체스판의 가로 세로의 세로의 길이 n이 매개변수로 주어질 때, n개의 퀸이 조건에 만족 하도록 배치할 수 있는 방법의 수를 return하는 solution함수를 완성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>퀸(Queen)은 가로, 세로, 대각선으로 이동할 수 있습니다.</li>
<li>n은 12이하의 자연수 입니다.</li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>n</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>4</td>
<td>2</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p>입출력 예 #1<br>
문제의 예시와 같습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://school.programmers.co.kr/learn/challenges

# 2차원 격자(ex.바둑판)에서 대각선인지 판단할 때 사용하는 아이디어
## `abs(row1 - row2) == abs(col1 - col2)` 가 대각선을 의미함!
### why? 우리가 생각하는 45도 대각선 -> **직선의 기울기**
- 45도 대각선 == 기울기(m)가 ±1 인 직선   
  ![image](https://github.com/user-attachments/assets/252e7928-75ae-4a99-86c3-6083365283dc)   
즉, ![image](https://github.com/user-attachments/assets/81b60d78-a493-48fc-b9e6-515cd0874daf) 이 성립하면 두 점이 대각서에 있다는 의미

#### 체스판같은 정수 좌표만 있는 격자에서는 기울기를 계산하는 대신, 행(row) 차이와 열(col) 차이만 비교하면 대각선 판별 가능
- 즉, ![image](https://github.com/user-attachments/assets/1b1ddb5b-2bd8-4059-85cf-bca1274e3b9d)이 성립하면 같은 대각선


