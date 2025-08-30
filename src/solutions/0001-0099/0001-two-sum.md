# 两数之和

# 一、问题描述

- 难度：简单
- 标签：数组、哈希表
- 原题：

> 给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** `target`  的那 **两个** 整数，并返回它们的数组下标。
>
> 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
>
> 你可以按任意顺序返回答案。

你老爸叫你去市场买菜，做个芹菜炒肉，你要买的 `target` 就是 `芹菜炒肉`，你不能买辣椒和肉回去，你也不忙买两份肉，因为不符合要求。

你必须在市场 `nums` 里面找到能做出 `taget` 芹菜炒肉的食材(`num` 元素)

还有个特殊的要求，是你要几下这些食材售卖的位置，也就是 `nums` 中符合要求的元素索引。

# 二、示例

## 案例一

输入：
- `nums = [2,7,11,15]`
- `target = 9`

输出：
- `[0,1]`

解释：
- 因为 $nums[0] + nums[1] == 9$ ，返回 $[0, 1]$。

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

----


> [!NOTE]
>
> 你可以在先在这里使用 rust 编辑

```rust,editable
fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    // 请在这里编辑
}

// 请勿更改下方代码
fn main() {
    // 测试用例
    let nums = vec![2, 7, 32, 4, 55, 12, 45, 67, 98, 11, 15];
    let target = 18;
    let result = two_sum(nums, target);
    println!("结果: {:?}", result);
}
```
# 四、解题
## 方法一：相同方式遍历
可以使用两组循环，分别遍历每一个数，检查他们的和是不是等于目标数组，因为不能两次使用相同的元素，所以还要检查元素的索引是否相同。

### 具体步骤：
1. 外层循环遍历数组的每个元素作为第一个数
2. 内层循环遍历数组的每个元素作为第二个数
3. 检查两个数的和是否等于目标值
4. 检查两个数的索引是否相同
5. 如果等于目标值并且索引不同，返回两个元素的索引
6. 如果遍历完所有组合都没找到，返回空结果

```python
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for id_i, i in enumerate(nums):
      for id_j, j in enumerate(nums):
        if target == i + j and id_i != id_j:
          return [id_i, id_j]
```

### 解析

**时间复杂度计算：**
- 外层循环执行 $n$ 次
- 内层循环每次执行 $n$ 次
- 总操作次数：$n × n = n^2$
- 时间复杂度：$O(n^2)$

**空间复杂度计算：**
- 只使用了常数个额外变量（`id_i`, `i`, `id_j`, `j`）
- 空间复杂度：$O(1)$

**这个代码的问题是：**

1. **效率低下**：每个元素都会与所有其他元素（包括自己）进行比较，存在大量无效比较
2. **重复计算**：会计算重复的组合，如 $(i,j)$ 和 $(j,i)$
3. **时间复杂度高**：$O(n^2)$ 对大数据集性能很差

**有没有更好的方案呢？**

有的，可以避免重复比较，优化内层循环的范围。



## 方法二：不重复遍历

通过优化循环范围，避免重复比较和自我比较，提高算法效率。

### 具体步骤：
1. 外层循环遍历数组的每个元素作为第一个数
2. 内层循环遍历当前元素之后的所有元素作为第二个数
3. 检查两个数的和是否等于目标值
4. 如果相等，返回两个元素的索引
5. 如果遍历完所有组合都没找到，返回空结果

```python
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
          return [i, j]
    return []
```

### 解析
**时间复杂度计算：**

- 外层循环执行 $n$ 次
- 内层循环平均执行 $(n-1) / 2$ 次
- 总比较次数：$n × (n-1)/2 ≈ n^2/2$
- 时间复杂度：$O(n²)$（仍是平方级，但相较于方法一，实际操作次数减少约一半）

**空间复杂度计算：**

- 只使用了常数个额外变量 $(i, j)$
- 空间复杂度：$O(1)$

**这个代码的问题是：**

1. **时间复杂度仍然较高**：虽然减少了一半比较次数，但仍是 $O(n^2)$
2. **大数据集性能差**：当数组很大时，仍然需要大量时间
3. **无法利用已访问信息**：没有记录之前遍历过的元素信息

**有没有更好的方案呢？**
当前在访问一个元素的时候，只是通过目标值找那个差值，如果记录当前的元素和索引，那么就不用每次拿到一个元素的时候，再去找差值。

而是通过当前元素获取到差值后，检查之前有没有这个值，如果有就返回索引。

好处是通过一层循环就可以实现，也就是说，可以使用哈希表来实现 $O(n)$ 时间复杂度。

## 方法三：哈希表单次遍历 🌟
利用哈希表的 $O(1)$ 查找特性，将时间复杂度优化到线性级别。

### 具体步骤：
1. 创建一个哈希表用于存储已访问的元素及其索引
2. 遍历数组的每个元素
3. 计算当前元素的补数（`target - 当前元素`）
4. 在哈希表中查找补数是否存在
5. 如果存在，返回补数的索引和当前元素索引
6. 如果不存在，将当前元素及其索引存入哈希表
7. 继续处理下一个元素

```python
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    hash_table = {}
    for i, num in enumerate(nums):
      complement = target - num
      if complement in hash_table:
        return [hash_table[complement], i]
      hash_table[num] = i
    return []
```

### 解析
**时间复杂度计算：**

- 单层循环执行 $n$ 次
- 哈希表查找和插入操作平均为 $O(1)$
- 总操作次数：约 $3n$（循环控制 + 计算补数 + 哈希操作）
- 时间复杂度：$O(n)$

**空间复杂度计算：**
- 哈希表最多存储 $n$ 个元素
- 空间复杂度：$O(n)$

**这个代码的优势：**

1. **时间效率最优**：线性时间复杂度，性能优秀
2. **一次遍历**：只需要遍历数组一次
3. **利用已访问信息**：通过哈希表记录并快速查找之前的元素

**还有没有更好的方法呢？**

目前来看已经没有了，但是存在一些比较偏门的方法，比如下面这个

## 方法四：排序 + 双指针（特殊）
如果不要求返回原始索引，或者可以创建索引映射，还可以使用排序配合双指针的方法。

### 具体步骤：
1. 创建元素值和原始索引的映射
2. 对数组进行排序
3. 使用左右双指针从两端向中间移动
4. 如果两指针元素和等于目标值，返回原始索引
5. 如果和小于目标值，左指针右移
6. 如果和大于目标值，右指针左移

```python
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    # 创建 (值, 原始索引) 的列表并排序
    indexed_nums = [(num, i) for i, num in enumerate(nums)]
    indexed_nums.sort()

    left, right = 0, len(nums) - 1
    while left < right:
      current_sum = indexed_nums[left][0] + indexed_nums[right][0]
      if current_sum == target:
        return [indexed_nums[left][1], indexed_nums[right][1]]
      elif current_sum < target:
        left += 1
      else:
        right -= 1
    return []
```

### 解析
**时间复杂度计算：**
- 创建索引列表：$O(n)$
- 排序操作：$O(n log n)$
- 双指针查找：$O(n)$
- 总时间复杂度：$O(n log n)$

**空间复杂度计算：**

- 需要额外数组存储索引信息
- 空间复杂度：$O(n)$



## 总结对比

| 方法 | 时间复杂度 | 空间复杂度 | 优点 | 缺点 | 适用场景 |
|------|------------|------------|------|------|----------|
| 方法一：全遍历 | O(n²) | O(1) | 简单直观 | 效率低，有重复计算 | 学习理解 |
| 方法二：优化遍历 | O(n²) | O(1) | 减少比较次数 | 仍然是平方复杂度 | 小数据集 |
| 方法三：哈希表 | O(n) | O(n) | 最优时间效率 | 需要额外空间 | **推荐方案** |
| 方法四：排序+双指针 | O(n log n) | O(n) | 思路优雅 | 需要排序开销 | 特定场景 |

**最佳实践建议：**

- **一般情况**：使用方法三（哈希表），时间效率最优
- **内存受限**：使用方法二（优化遍历），空间复杂度为 O(1)
- **学习目的**：从方法一开始理解，逐步优化到方法三
- **面试场景**：能够分析多种方法的优劣，展示算法思维过程

哈希表方法在时间和空间之间取得了最好的平衡，是实际应用中的首选方案。



# 五、动画演示

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
<p class="twosum-title">"两数之和" 动画演示</h1>
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
<p class="twosum-section-title">输入数组 nums</h2>
<div id="array-container" class="twosum-array-container">
</div>
</div>
<div>
<p class="twosum-section-title">哈希表 hashMap</h2>
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



# 六、Rust 时间复杂度解析

## $O(N^2)$ 算法

```rust
# use std::time::Instant;
#
# // 全局操作计数器
# static mut OPERATION_COUNT: u64 = 0;
#
# fn count_op() {
#     unsafe {
#         OPERATION_COUNT += 1;
#     }
# }
#
# fn reset_counter() {
#     unsafe {
#         OPERATION_COUNT = 0;
#     }
# }
#
# fn get_count() -> u64 {
#     unsafe { OPERATION_COUNT }
# }
#
# // Two Sum O(n²) 实现
 fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
#     // 外层循环 - 遍历每个元素
     for i in 0..nums.len() {
#         count_op(); // 外层循环操作
#
#         // 内层循环 - 遍历剩余元素
         for j in (i + 1)..nums.len() {
#             count_op(); // 内层循环操作
#             count_op(); // 数组访问 nums[i]
#             count_op(); // 数组访问 nums[j]
#             count_op(); // 加法操作
#             count_op(); // 比较操作
#
             if nums[i] + nums[j] == target {
#                 count_op(); // 找到结果的操作
                 return vec![i as i32, j as i32];
             }
         }
     }
#
#     count_op(); // 未找到结果
     vec![] // 返回空向量表示未找到
 }
#
# // 时间复杂度分析器
# fn analyze_complexity(sizes: &[usize], operation_counts: &[u64], times: &[u128]) {
#     println!("\n=== O(n²) 时间复杂度分析 ===");
#
#     if sizes.len() < 2 {
#         return;
#     }
#
#     // 分析操作次数增长
#     let first_size = sizes[0];
#     let last_size = sizes[sizes.len() - 1];
#     let first_ops = operation_counts[0];
#     let last_ops = operation_counts[operation_counts.len() - 1];
#
#     let size_ratio = last_size as f64 / first_size as f64;
#     let ops_ratio = last_ops as f64 / first_ops as f64;
#     let theoretical_n2_ratio = size_ratio * size_ratio;
#
#     println!("输入规模变化: {} -> {} (×{:.1})", first_size, last_size, size_ratio);
#     println!("操作次数变化: {} -> {} (×{:.1})", first_ops, last_ops, ops_ratio);
#     println!("理论 n² 增长: ×{:.1}", theoretical_n2_ratio);
#
#     // 判断是否符合 O(n²)
#     let difference_ratio = (ops_ratio - theoretical_n2_ratio).abs() / theoretical_n2_ratio;
#     if difference_ratio < 0.3 {
#         println!("✅ 符合 O(n²) 时间复杂度特征");
#     } else {
#         println!("❌ 不完全符合 O(n²) 模式 (差异: {:.1}%)", difference_ratio * 100.0);
#     }
#
#     // 显示详细增长趋势
#     println!("\n增长趋势分析:");
#     println!("规模 | 操作数 | 理论n² | 实际/理论 | 执行时间");
#     println!("-----|--------|--------|----------|----------");
#
#     for i in 0..sizes.len() {
#         let n = sizes[i] as f64;
#         let theoretical_ops = (n * (n - 1.0) / 2.0) as u64; // n(n-1)/2 次比较
#         let actual_ops = operation_counts[i];
#         let ratio = actual_ops as f64 / theoretical_ops as f64;
#
#         println!("{:4} | {:6} | {:6} | {:8.2} | {:6.2}μs",
#                  sizes[i], actual_ops, theoretical_ops, ratio, times[i]);
#     }
# }
#
# // 生成测试数据
# fn generate_test_data(size: usize) -> Vec<i32> {
#     // 生成 1 到 size 的数组，最后两个元素的和作为目标
#     (1..=size as i32).collect()
# }
#
# fn main() {
#     println!("=== Two Sum O(n²) 算法实现与复杂度分析 ===");
#     // 测试不同规模的数据
#     let test_sizes = vec![5, 10, 20, 50, 100];
#     let mut operation_counts = Vec::new();
#     let mut execution_times = Vec::new();
#
#     println!("=== 测试结果 ===");
#    println!("数组大小 \t| 操作次数 \t| 执行时间 \t| 结果\t\t\t\t| 测试数组 \t\t\t\t| 目标数字");
#    println!("--------\t|--------\t|---------\t|-----\t\t\t\t|--------\t\t\t\t|--------");
#
#     for &size in &test_sizes {
#         let nums = generate_test_data(size);
#         let target = nums[size-2] + nums[size-1]; // 倒数第二个和最后一个元素的和
#
#         reset_counter();
#         let start = Instant::now();
#         let result = two_sum(nums.clone(), target);
#         let duration = start.elapsed();
#
#         let ops = get_count();
#         let time_us = duration.as_micros();
#
#         operation_counts.push(ops);
#         execution_times.push(time_us);
#
#         match result.len() {
#             2 => {
#                 let i = result[0] as usize;
#                 let j = result[1] as usize;
#                 println!("{:8} \t| {:8} \t| {:8.2}μs \t| 找到: [{}]={}, [{}]={} \t| {:?} \t| {:#?}",size, ops, time_us, i, nums[i], j, nums[j],nums,target);
#              }
#             _ => {
#                 println!("{:8} | {:8} | {:8.2}μs | 未找到",
#                         size, ops, time_us);
#             }
#         }
#     }
#
#     // 分析时间复杂度
#     analyze_complexity(&test_sizes, &operation_counts, &execution_times);
#
#
#     println!("\n=== 性能总结 ===");
#     if let (Some(&first_size), Some(&last_size)) = (test_sizes.first(), test_sizes.last()) {
#         if let (Some(&first_ops), Some(&last_ops)) = (operation_counts.first(), operation_counts.last()) {
#             let size_increase = last_size as f64 / first_size as f64;
#             let ops_increase = last_ops as f64 / first_ops as f64;
#             println!("输入规模增加 {:.1} 倍时，操作次数增加 {:.1} 倍", size_increase, ops_increase);
#         }
#     }
# }
```

- 嵌套循环: 外层循环 n 次，内层循环平均 n/2 次
- 总比较次数: n(n-1)/2 ≈ n²/2
- 随输入规模 n 增长，操作次数按 n² 增长
- 最坏情况: 目标不存在，需要检查所有组合
- 最好情况: 第一对就是答案，但时间复杂度仍是 O(n²)

程序序中的基本操作包括:
- 外层循环控制
- 内层循环控制
- 数组元素访问 (`nums[i]`, `nums[j]`)
- 算术运算 (加法)
- 比较操作 (相等判断)
- 条件分支判断



##  $O(N)$ 算法
```rust
# use std::time::Instant;
#
# // 全局操作计数器
# static mut OPERATION_COUNT: u64 = 0;
#
# fn count_op() {
#     unsafe {
#         OPERATION_COUNT += 1;
#     }
# }
#
# fn reset_counter() {
#     unsafe {
#         OPERATION_COUNT = 0;
#     }
# }
#
# fn get_count() -> u64 {
#     unsafe { OPERATION_COUNT }
# }
#
# // Two Sum O(n) 实现 - 使用哈希表
 fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
     use std::collections::HashMap;
#
     let mut map = HashMap::new();
#     count_op(); // 创建HashMap
#
#     // 单层循环 - 遍历每个元素
     for (i, num) in nums.iter().enumerate() {
#         count_op(); // 循环操作
#
         let complement = target - num;
#         count_op(); // 减法操作
#
#         // 检查补数是否在哈希表中
#         count_op(); // HashMap查找操作
         if let Some(&j) = map.get(&complement) {
#             count_op(); // 找到结果的操作
             return vec![j as i32, i as i32];
         }
#
#         // 将当前元素和索引存入哈希表
#         count_op(); // HashMap插入操作
         map.insert(num, i);
     }
#
#     count_op(); // 未找到结果
     vec![] // 返回空向量表示未找到
 }
#
# // 时间复杂度分析器
# fn analyze_complexity(sizes: &[usize], operation_counts: &[u64], times: &[u128]) {
#     println!("\n=== O(n) 时间复杂度分析 ===");
#
#     if sizes.len() < 2 {
#         return;
#     }
#
#     // 分析操作次数增长
#     let first_size = sizes[0];
#     let last_size = sizes[sizes.len() - 1];
#     let first_ops = operation_counts[0];
#     let last_ops = operation_counts[operation_counts.len() - 1];
#
#     let size_ratio = last_size as f64 / first_size as f64;
#     let ops_ratio = last_ops as f64 / first_ops as f64;
#     let theoretical_n_ratio = size_ratio; // O(n) 线性增长
#
#     println!("输入规模变化: {} -> {} (×{:.1})", first_size, last_size, size_ratio);
#     println!("操作次数变化: {} -> {} (×{:.1})", first_ops, last_ops, ops_ratio);
#     println!("理论 n 增长: ×{:.1}", theoretical_n_ratio);
#
#     // 判断是否符合 O(n)
#     let difference_ratio = (ops_ratio - theoretical_n_ratio).abs() / theoretical_n_ratio;
#     if difference_ratio < 0.5 {
#         println!("✅ 符合 O(n) 时间复杂度特征");
#     } else {
#         println!("❌ 不完全符合 O(n) 模式 (差异: {:.1}%)", difference_ratio * 100.0);
#     }
#
#     // 显示详细增长趋势
#     println!("\n增长趋势分析:");
#     println!("规模 | 操作数 | 理论n | 实际/理论 | 执行时间");
#     println!("-----|--------|-------|----------|----------");
#
#     for i in 0..sizes.len() {
#         let n = sizes[i] as f64;
#         let theoretical_ops = (n * 3.0) as u64; // 大约每个元素3次操作
#         let actual_ops = operation_counts[i];
#         let ratio = actual_ops as f64 / theoretical_ops as f64;
#
#         println!("{:4} | {:6} | {:5} | {:8.2} | {:6.2}μs",
#                  sizes[i], actual_ops, theoretical_ops, ratio, times[i]);
#     }
# }
#
# // 生成测试数据
# fn generate_test_data(size: usize) -> Vec<i32> {
#     // 生成 1 到 size 的数组，最后两个元素的和作为目标
#     (1..=size as i32).collect()
# }
#
# fn main() {
#     println!("=== Two Sum O(n) 算法实现与复杂度分析 ===");
#
#     // 测试不同规模的数据
#     let test_sizes = vec![5, 10, 20, 50, 100];
#     let mut operation_counts = Vec::new();
#     let mut execution_times = Vec::new();
#
#     println!("=== 测试结果 ===");
#         println!("数组大小 \t| 操作次数 \t| 执行时间 \t| 结果\t\t\t\t| 测试数组 \t\t\t\t| 目标数字");
#         println!("--------\t|--------\t|---------\t|-----\t\t\t\t|--------\t\t\t\t|--------");
#
#     for &size in &test_sizes {
#         let nums = generate_test_data(size);
#         let target = nums[size-2] + nums[size-1]; // 倒数第二个和最后一个元素的和
#
#         reset_counter();
#         let start = Instant::now();
#         let result = two_sum(nums.clone(), target);
#         let duration = start.elapsed();
#
#         let ops = get_count();
#         let time_us = duration.as_micros();
#
#         operation_counts.push(ops);
#         execution_times.push(time_us);
#
#         match result.len() {
#             2 => {
#                 let i = result[0] as usize;
#                 let j = result[1] as usize;
#                 println!("{:8} \t| {:8} \t| {:8.2}μs \t| 找到: [{}]={}, [{}]={} \t| {:?} \t| {:#?}",size, ops, time_us, i, nums[i], j, nums[j],nums,target);
#             }
#             _ => {
#                 println!("{:8} | {:8} | {:8.2}μs | 未找到",
#                         size, ops, time_us);
#             }
#         }
#     }
#
#     // 分析时间复杂度
#     analyze_complexity(&test_sizes, &operation_counts, &execution_times);
#

#     println!("\n=== 性能总结 ===");
#     if let (Some(&first_size), Some(&last_size)) = (test_sizes.first(), test_sizes.last()) {
#         if let (Some(&first_ops), Some(&last_ops)) = (operation_counts.first(),  operation_counts.last()) {
#             let size_increase = last_size as f64 / first_size as f64;
#             let ops_increase = last_ops as f64 / first_ops as f64;
#             println!("输入规模增加 {:.1} 倍时，操作次数增加 {:.1} 倍", size_increase, ops_increase);
#         }
#     }
# }
```

- 单层循环: 只遍历数组一次
- 哈希表查找: O(1) 平均时间复杂度
- 总时间复杂度: O(n) 线性时间
- 空间复杂度: O(n) - 需要额外的哈希表存储
- 最坏情况: 遍历整个数组，操作次数与 n 成正比
- 最好情况: 第二个元素就找到答案，但仍是 O(n)



## 内存访问模式

**暴力解法**：

- 顺序访问数组元素，缓存友好
- 内存访问模式可预测
- 没有随机内存访问

**哈希表解法**：
- 哈希表访问可能导致缓存miss
- 内存访问模式相对随机
- 对CPU缓存不够友好


在现代计算环境下，除非有特殊的空间限制，否则哈希表解法通常是更好的选择。O(n) 与 O(n²) 的性能差异在大数据场景下是巨大的，而额外的 O(n) 空间开销在现代硬件条件下通常是可以接受的。

这个题到这里就结束了，相信你一定有自己的收获！

如果你是算法和数据结构的新手，建议在刷 LeetCode 之前先学习一下基础知识，这样刷题时会更顺利。
