# 两数之和

# 一、问题描述

- 难度：简单
- 标签：数组、哈希表
- 原题：[中文](https://leetcode.cn/problems/two-sum/) | [English](https://leetcode.com/problems/two-sum/)

> 给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** `target`  的那 **两个** 整数，并返回它们的数组下标。
>
> 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
>
> 你可以按任意顺序返回答案。



# 二、示例

## 案例一

输入：
- `nums = [2,7,11,15]`
- `target = 9`

输出：
- `[0,1]`

解释：
- 因为 \\( nums[0] + nums[1] == 9 \\) ，返回 \\( [0, 1] \\)。

## 案例二

输入：
- `nums = [3,2,4]`
- `target = 6`

输出：
- `[1,2]`

## 案例三

输入：
- `nums = [3,3]`
- `target = 6`

输出：
- `[0,1]`

---

# 三、提示

- `2 <= nums.length <= 104`
- `-109 <= nums[i] <= 109`
- `-109 <= target <= 109`

只会存在一个有效答案

---

你可以在这里使用 rust 尝试：

```rust,editable
fn main(){
    println!("hello")
}
```



# 四、进阶

> 你可以想出一个时间复杂度小于 \\( O(n^2) \\) 的算法吗？

```rust,editable
fn main(){
    println!("hello")
}
```

# 五、解析


# 六、解题案例

# 七、动画演示

> GitHub 地址： https://github.com/ChenQiWen/lc-1

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>"两数之和"动画演示 - 哈希表解法</title>
<style>
.twosum-demo-container {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans SC", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
}
.twosum-demo-container * {
box-sizing: border-box;
}
.twosum-demo-container {
background-color: #f3f4f6;
display: flex;
align-items: center;
justify-content: center;
padding: 1rem;
}
.twosum-main-card {
width: 100%;
max-width: 80rem;
margin: 0 auto;
background-color: white;
border-radius: 1rem;
box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
padding: 1.5rem;
}
@media (min-width: 768px) {
.twosum-main-card {
padding: 2rem;
}
}
.twosum-header {
text-align: center;
margin-bottom: 2rem;
}
.twosum-title {
font-size: 1.5rem;
font-weight: 700;
color: #1f2937;
margin-bottom: 0.5rem;
}
@media (min-width: 768px) {
.twosum-title {
font-size: 1.875rem;
}
}
.twosum-subtitle {
color: #6b7280;
margin-top: 0.5rem;
}
.twosum-control-grid {
display: grid;
grid-template-columns: 1fr;
gap: 1rem;
margin-bottom: 2rem;
padding: 1rem;
background-color: #f9fafb;
border-radius: 0.5rem;
border: 1px solid #e5e7eb;
align-items: end;
}
@media (min-width: 640px) {
.twosum-control-grid {
grid-template-columns: repeat(2, 1fr);
}
}
@media (min-width: 1024px) {
.twosum-control-grid {
grid-template-columns: repeat(6, 1fr);
}
}
.twosum-input-group-large {
grid-column: span 1;
}
@media (min-width: 640px) {
.twosum-input-group-large {
grid-column: span 2;
}
}
@media (min-width: 1024px) {
.twosum-input-group-large {
grid-column: span 3;
}
}
.twosum-input-group-medium {
grid-column: span 1;
}
@media (min-width: 640px) {
.twosum-input-group-medium {
grid-column: span 2;
}
}
@media (min-width: 1024px) {
.twosum-input-group-medium {
grid-column: span 1;
}
}
.twosum-input-group-small {
grid-column: span 1;
}
.twosum-label {
display: block;
font-size: 0.875rem;
font-weight: 600;
color: #374151;
margin-bottom: 0.25rem;
}
.twosum-input {
display: block;
width: 100%;
border-radius: 0.5rem;
border: 1px solid #d1d5db;
box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
padding: 0.75rem;
font-size: 0.875rem;
transition: border-color 150ms ease-in-out, box-shadow 150ms ease-in-out;
}
.twosum-input:focus {
outline: none;
border-color: #6366f1;
box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.3);
}
.twosum-btn {
width: 100%;
font-weight: 700;
padding: 0.5rem 1rem;
border-radius: 0.5rem;
border: none;
cursor: pointer;
transition: all 150ms ease-in-out;
box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
}
.twosum-btn:hover {
box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}
.twosum-btn:active {
transform: scale(0.95);
}
.twosum-btn:focus {
outline: none;
box-shadow: 0 0 0 2px rgba(0, 0, 0, 0.05), 0 0 0 4px rgba(156, 163, 175, 0.5);
}
.twosum-btn-gray {
background-color: #6b7280;
color: white;
}
.twosum-btn-gray:hover {
background-color: #4b5563;
}
.twosum-btn-gray:focus {
box-shadow: 0 0 0 2px rgba(0, 0, 0, 0.05), 0 0 0 4px rgba(156, 163, 175, 0.5);
}
.twosum-btn-indigo {
background-color: #4f46e5;
color: white;
}
.twosum-btn-indigo:hover {
background-color: #4338ca;
}
.twosum-btn-indigo:focus {
box-shadow: 0 0 0 2px rgba(0, 0, 0, 0.05), 0 0 0 4px rgba(79, 70, 229, 0.5);
}
.twosum-btn:disabled {
opacity: 0.5;
cursor: not-allowed;
}
.twosum-status-box {
margin-bottom: 2rem;
padding: 1rem;
text-align: center;
background-color: #eff6ff;
color: #1e40af;
border-radius: 0.5rem;
min-height: 5rem;
display: flex;
align-items: center;
justify-content: center;
border: 1px solid #bfdbfe;
}
.twosum-status-text {
font-size: 1.125rem;
font-weight: 500;
}
.twosum-display-grid {
display: grid;
grid-template-columns: 1fr;
gap: 2rem;
}
@media (min-width: 1024px) {
.twosum-display-grid {
grid-template-columns: repeat(2, 1fr);
}
}
.twosum-section-title {
font-size: 1.25rem;
font-weight: 600;
color: #374151;
margin-bottom: 1rem;
text-align: center;
}
.twosum-array-container {
display: flex;
flex-wrap: wrap;
gap: 0.5rem;
justify-content: center;
padding: 1rem;
background-color: #f3f4f6;
border-radius: 0.5rem;
min-height: 5rem;
}
.twosum-hash-container {
padding: 1rem;
background-color: #f3f4f6;
border-radius: 0.5rem;
min-height: 5rem;
}
.twosum-hash-container > * + * {
margin-top: 0.5rem;
}
.twosum-array-element {
width: 5rem;
height: 5rem;
background-color: white;
border-radius: 0.5rem;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
border: 1px solid #e5e7eb;
transition: all 0.5s ease-in-out;
}
.twosum-array-element .index {
font-size: 0.75rem;
color: #6b7280;
}
.twosum-array-element .value {
font-size: 1.5rem;
font-weight: 700;
color: #1f2937;
}
.twosum-hash-map-entry {
background-color: white;
padding: 0.5rem;
border-radius: 0.5rem;
box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
display: flex;
justify-content: space-between;
align-items: center;
border: 1px solid #e5e7eb;
transition: all 0.5s ease-in-out;
}
.twosum-hash-key {
font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, "Liberation Mono", Menlo, monospace;
background-color: #e0e7ff;
color: #3730a3;
padding: 0.25rem 0.5rem;
border-radius: 0.25rem;
}
.twosum-hash-value {
font-family: ui-monospace, SFMono-Regular, "SF Mono", Consolas, "Liberation Mono", Menlo, monospace;
background-color: #fce7f3;
color: #be185d;
padding: 0.25rem 0.5rem;
border-radius: 0.25rem;
}
.twosum-highlight-current {
background-color: #3b82f6 !important;
color: white !important;
transform: translateY(-10px);
}
.twosum-highlight-current .index,
.twosum-highlight-current .value {
color: white !important;
}
.twosum-highlight-found {
background-color: #22c55e !important;
color: white !important;
transform: scale(1.1);
}
.twosum-highlight-found .index,
.twosum-highlight-found .value {
color: white !important;
}
.twosum-highlight-lookup {
background-color: #eab308 !important;
color: white !important;
}
.twosum-fade-in {
animation: twosum-fadeIn 0.5s ease-in-out forwards;
}
@keyframes twosum-fadeIn {
from {
opacity: 0;
transform: translateY(20px);
}
to {
opacity: 1;
transform: translateY(0);
}
}
.twosum-text-green {
color: #059669;
}
.twosum-text-bold {
font-weight: 700;
}
.twosum-text-xl {
font-size: 1.25rem;
}
</style>
</head>
<body>
<div class="twosum-demo-container">
<div class="twosum-main-card">
<header class="twosum-header">
<h1 class="twosum-title">"两数之和"动画演示</h1>
<p class="twosum-subtitle">通过哈希表实现 O(n) 时间复杂度</p>
</header>
<div class="twosum-control-grid">
<div class="twosum-input-group-large">
<label for="nums-input" class="twosum-label">输入数组 (nums)</label>
<input type="text" id="nums-input" class="twosum-input" value="2, 7, 11, 15">
</div>
<div class="twosum-input-group-medium">
<label for="target-input" class="twosum-label">目标值 (target)</label>
<input type="number" id="target-input" class="twosum-input" value="9">
</div>
<div class="twosum-input-group-small">
<button id="random-btn" class="twosum-btn twosum-btn-gray">随机生成</button>
</div>
<div class="twosum-input-group-small">
<button id="start-btn" class="twosum-btn twosum-btn-indigo">开始</button>
</div>
</div>
<div id="status-box" class="twosum-status-box">
<p id="status-text" class="twosum-status-text">点击"开始"以查看算法执行过程。</p>
</div>
<div class="twosum-display-grid">
<div>
<h2 class="twosum-section-title">输入数组 `nums`</h2>
<div id="array-container" class="twosum-array-container">
</div>
</div>
<div>
<h2 class="twosum-section-title">哈希表 `hashMap`</h2>
<div id="hash-map-container" class="twosum-hash-container">
</div>
</div>
</div>
</div>
</div>
<script>
const numsInput = document.getElementById('nums-input');
const targetInput = document.getElementById('target-input');
const startBtn = document.getElementById('start-btn');
const randomBtn = document.getElementById('random-btn');
const arrayContainer = document.getElementById('array-container');
const hashMapContainer = document.getElementById('hash-map-container');
const statusText = document.getElementById('status-text');
let isAnimating = false;
const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));
function generateRandomData() {
if (isAnimating) return;
const len = Math.floor(Math.random() * 7) + 4; // 数组长度 4-10
const uniqueNums = new Set();
while(uniqueNums.size < len) {
uniqueNums.add(Math.floor(Math.random() * 40) + 1); // 数值 1-40
}
const nums = Array.from(uniqueNums);
let index1 = Math.floor(Math.random() * len);
let index2 = Math.floor(Math.random() * len);
while (index1 === index2) {
index2 = Math.floor(Math.random() * len);
}
const target = nums[index1] + nums[index2];
numsInput.value = nums.join(', ');
targetInput.value = target;
setup();
}
function setup() {
const numsStr = numsInput.value.trim();
if (!numsStr) {
statusText.textContent = "请输入有效的数组。";
return;
}
const nums = numsStr.split(',').map(n => parseInt(n.trim())).filter(n => !isNaN(n));
const target = parseInt(targetInput.value);
if (nums.length < 2) {
statusText.textContent = "数组长度必须至少为 2。";
return;
}
if (isNaN(target)) {
statusText.textContent = "请输入有效的目标值。";
return;
}
arrayContainer.innerHTML = '';
hashMapContainer.innerHTML = '';
statusText.textContent = '准备就绪。点击"开始"以进行演示。';
startBtn.textContent = '开始';
nums.forEach((num, index) => {
const element = document.createElement('div');
element.className = 'twosum-array-element';
element.id = `array-el-${index}`;
element.innerHTML = `<span class="index">索引 ${index}</span><span class="value">${num}</span>`;
arrayContainer.appendChild(element);
});
return { nums, target };
}
async function startAnimation() {
if (isAnimating) return;
isAnimating = true;
startBtn.disabled = true;
randomBtn.disabled = true;
startBtn.textContent = '演示中...';
startBtn.classList.add('twosum-btn-disabled');
randomBtn.classList.add('twosum-btn-disabled');
const initialState = setup();
if (!initialState) {
isAnimating = false;
startBtn.disabled = false;
randomBtn.disabled = false;
startBtn.textContent = '开始';
startBtn.classList.remove('twosum-btn-disabled');
randomBtn.classList.remove('twosum-btn-disabled');
return;
}
const { nums, target } = initialState;
const hashMap = {};
for (let i = 0; i < nums.length; i++) {
const currentNum = nums[i];
const complement = target - currentNum;
const currentEl = document.getElementById(`array-el-${i}`);
statusText.textContent = `第 ${i+1} 步：遍历到索引 ${i}，值为 ${currentNum}。`;
currentEl.classList.add('twosum-highlight-current');
await sleep(1500);
statusText.innerHTML = `正在计算配对目标 (complement): <br> <span class="twosum-text-bold twosum-text-xl">${target} - ${currentNum} = ${complement}</span>`;
await sleep(1500);
statusText.textContent = `在哈希表中查找是否存在键(key)为 ${complement} 的项...`;
const complementEntry = document.getElementById(`hash-entry-${complement}`);
if (complementEntry) {
complementEntry.classList.add('twosum-highlight-lookup');
}
await sleep(1500);
if (hashMap[complement] !== undefined) {
const complementIndex = hashMap[complement];
const complementEl = document.getElementById(`array-el-${complementIndex}`);
statusText.textContent = `成功！在哈希表中找到 ${complement}，其下标为 ${complementIndex}。`;
complementEntry.classList.remove('lookup');
complementEntry.classList.add('twosum-highlight-found');
currentEl.classList.remove('twosum-highlight-current');
currentEl.classList.add('twosum-highlight-found');
complementEl.classList.add('twosum-highlight-found');
statusText.innerHTML = `<span class="twosum-text-green twosum-text-bold twosum-text-xl">找到配对！因为 nums[${complementIndex}] + nums[${i}] = ${target}。返回 [${complementIndex}, ${i}]</span>`;
isAnimating = false;
startBtn.disabled = false;
randomBtn.disabled = false;
startBtn.textContent = '重新开始';
startBtn.classList.remove('twosum-btn-disabled');
randomBtn.classList.remove('twosum-btn-disabled');
return;
} else {
if (complementEntry) complementEntry.classList.remove('twosum-highlight-lookup');
statusText.textContent = `未找到 ${complement}。准备将当前元素 ${currentNum} 添加到哈希表中。`;
await sleep(1500);
hashMap[currentNum] = i;
const newEntry = document.createElement('div');
newEntry.className = 'twosum-hash-map-entry';
newEntry.style.opacity = '0';
newEntry.id = `hash-entry-${currentNum}`;
newEntry.innerHTML = `
<span class="twosum-hash-key">key: ${currentNum}</span>
<span class="twosum-hash-value">value: ${i}</span>
`;
hashMapContainer.appendChild(newEntry);
await sleep(100);
newEntry.classList.add('twosum-fade-in');
statusText.textContent = `已将 { ${currentNum}: ${i} } 添加到哈希表中。`;
await sleep(1500);
}
currentEl.classList.remove('twosum-highlight-current');
}
statusText.textContent = "遍历完成，未找到符合条件的两个数。";
isAnimating = false;
startBtn.disabled = false;
randomBtn.disabled = false;
startBtn.textContent = '重新开始';
startBtn.classList.remove('twosum-btn-disabled');
randomBtn.classList.remove('twosum-btn-disabled');
}
startBtn.addEventListener('click', startAnimation);
randomBtn.addEventListener('click', generateRandomData);
window.onload = setup;
</script>
</body>