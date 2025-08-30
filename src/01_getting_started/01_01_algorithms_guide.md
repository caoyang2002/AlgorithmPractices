# 算法简易入门

# 一、两数之和

> LeetCode 第一题

# 二、题目链接

- LeetCode：[中文](https://leetcode.cn/problems/two-sum/) | [English](https://leetcode.com/problems/two-sum/)
- 本文档：[题目详情](../solutions/0001-0001/0001-add-sum.md)

# 三、问题描述

- 难度：简单
- 标签：数组、哈希表

> 给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** `target`  的那 **两个** 整数，并返回它们的数组下标。
>
> 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
>
> 你可以按任意顺序返回答案。

你老爸叫你去市场买菜，做个芹菜炒肉，你要买的 `target` 就是 `芹菜炒肉`，你不能买辣椒和肉回去，你也不忙买两份肉，因为不符合要求。

你必须在市场 `nums` 里面找到能做出 `taget` 芹菜炒肉的食材(`num` 元素)

还有个特殊的要求，是你要几下这些食材售卖的位置，也就是 `nums` 中符合要求的元素索引。

# 四、示例

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

# 五、提示

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
# 六、解题
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



# 七、Rust 时间复杂度解析

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



# 八、基础知识

## 数据结构

- 数组
- 字符串
- 链表
- 树

## 算法

- 分治

- 贪心

- 回溯

- 动态规划



# 九、算法书推荐

- 【书籍】[算法（第 4 版）- 谢路云 译](https://book.douban.com/subject/19952400/)
- 【书籍】[大话数据结构 - 程杰 著](https://book.douban.com/subject/6424904/)
- 【书籍】[趣学算法 - 陈小玉 著](https://book.douban.com/subject/27109832/)
- 【书籍】[算法图解 - 袁国忠 译](https://book.douban.com/subject/26979890/)
- 【书籍】[算法竞赛入门经典（第 2 版） - 刘汝佳 著](https://book.douban.com/subject/25902102/)
- 【书籍】[数据结构与算法分析 - 冯舜玺 译](https://book.douban.com/subject/1139426/)
- 【书籍】[算法导论（原书第 3 版） - 殷建平 / 徐云 / 王刚 / 刘晓光 / 苏明 / 邹恒明 / 王宏志 译](https://book.douban.com/subject/20432061/)





























<!--

## 1. LeetCode 是什么

**「LeetCode」** 是一个在线编程评测平台，主要包含算法、数据库、Shell、多线程等题目，其中以算法题目为主。LeetCode 上有 $3000+$ 道编程问题，支持 $16+$ 种编程语言，还有一个活跃的社区用于技术交流。我们可以通过解决 LeetCode 题库中的问题来练习编程技能，以及提高算法能力。

许多知名互联网公司在面试时会考察 LeetCode 题目，要求面试者分析问题、编写代码，并分析算法的时间复杂度和空间复杂度。通过 LeetCode 刷题，充分准备算法知识，对获得好的工作机会很有帮助。

## 2. LeetCode 新手入门

### 2.1 LeetCode 注册

1. 打开 LeetCode 中文主页，链接：[力扣（LeetCode）官网](https://leetcode.cn/)。
2. 输入手机号，获取验证码。
3. 输入验证码之后，点击「登录 / 注册」，就注册好了。

![LeetCode 注册页面](https://qcdn.itcharge.cn/images/20210901155409.png)

### 2.2 LeetCode 题库

「[题库](https://leetcode.cn/problemset/algorithms/)」是 LeetCode 上最直接的练习入口，在这里可以根据题目的标签、难度、状态进行刷题。也可以按照随机一题开始刷题。

![LeetCode 题库页面](https://qcdn.itcharge.cn/images/20210901155423.png)

#### 2.2.1 题目标签

LeetCode 的题目涉及了许多算法和数据结构。有贪心，搜索，动态规划，链表，二叉树，哈希表等等，可以通过选择对应标签进行专项刷题，同时也可以看到对应专题的完成度情况。

![LeetCode 题目标签](https://qcdn.itcharge.cn/images/20210901155435.png)

#### 2.2.2 题目列表

LeetCode 提供了题目的搜索过滤功能。可以筛选相关题单、不同难易程度、题目完成状态、不同标签的题目。还可以根据题目编号、题解数目、通过率、难度、出现频率等进行排序。

![LeetCode 题目列表](https://qcdn.itcharge.cn/images/20210901155450.png)

#### 2.2.3 当前进度

当前进度提供了一个直观的进度展示。在这里可以看到自己的练习概况。进度会自动展现当前的做题情况。也可以点击「[进度设置](https://leetcode.cn/session/)」创建新的进度，在这里还可以修改、删除相关的进度。

![LeetCode 当前进度](https://qcdn.itcharge.cn/images/20210901155500.png)

#### 2.2.4 题目详情

从题目列表点击进入，就可以看到这道题目的内容描述和代码编辑器。在这里还可以查看相关的题解和自己的提交记录。

![LeetCode 题目详情](https://qcdn.itcharge.cn/images/20210901155529.png)

### 2.3 LeetCode 刷题语言

面试时考察的是算法基本功，对于语言的选择没有限制。建议使用熟悉的语言或语法简洁的语言刷题。

相对于 Python 而言，C、C++ 语法比较复杂，在做题的时候除了要思考思路，还得考虑语法，不太利于刷题。Python 等语言更简洁，能让你专注于算法思路本身，提高刷题效率。当然，算法竞赛选手通常使用 C++，已经成为传统了。

> 人生苦短，我用 Python。

### 2.4 LeetCode 刷题流程

在「2.2.1 题目标签」中我们介绍了题目的相关情况。

![LeetCode 题目详情](https://qcdn.itcharge.cn/images/20210901155529.png)

可以看到左侧区域为题目内容描述区域，还可以看到题目的内容描述和一些示例数据。而右侧是代码编辑区域，代码编辑区域里边默认显示了待实现的方法。

我们需要在代码编辑器中根据方法给定的参数实现对应的算法，并返回题目要求的结果。然后还要经过「执行代码」测试结果，点击「提交」后，显示执行结果为「**通过**」时，才算完成一道题目。

![LeetCode 提交记录](https://qcdn.itcharge.cn/images/20210901155545.png)

总结一下我们的刷题流程为：

1. 在 LeetCode 题库中选择一道自己想要解决的题目。
2. 查看题目左侧的题目描述，理解题目要求。
3. 思考解决思路，并在右侧代码编辑区域实现对应的方法，并返回题目要求的结果。
4. 如果实在想不出解决思路，可以查看题目相关的题解，努力理解他人的解题思路和代码。
5. 点击「执行代码」按钮测试结果。
   - 如果输出结果与预期结果不符，则回到第 3 步重新思考解决思路，并改写代码。
6. 如果输出结果与预期符合，则点击「提交」按钮。
   - 如果执行结果显示「编译出错」、「解答错误」、「执行出错」、「超出时间限制」、「超出内存限制」等情况，则需要回到第 3 步重新思考解决思路，或者思考特殊数据，并改写代码。
7. 如果执行结果显示「通过」，恭喜你通过了这道题目。

接下来我们将通过「[2235. 两整数相加 - 力扣（LeetCode）](https://leetcode.cn/problems/add-two-integers/)」这道题目来讲解如何在 LeetCode 上刷题。

### 2.5 LeetCode 第一题

#### 2.5.1 题目链接

- [2235. 两整数相加 - 力扣（LeetCode）](https://leetcode.cn/problems/add-two-integers/)

#### 2.5.2 题目大意

**描述**：给定两个整数 $num1$ 和 $num2$。

**要求**：返回这两个整数的和。

**说明**：

- $-100 \le num1, num2 \le 100$。

**示例**：

- 示例 1：

```python
输入：num1 = 12, num2 = 5
输出：17
解释：num1 是 12，num2 是 5，它们的和是 12 + 5 = 17，因此返回 17。
```

- 示例 2：

```python
输入：num1 = -10, num2 = 4
输出：-6
解释：num1 + num2 = -6，因此返回 -6。
```

#### 2.5.3 解题思路

##### 思路 1：直接计算

1. 直接计算整数 $num1$ 与 $num2$ 的和，返回 $num1 + num2$ 即可。

##### 思路 1：代码

```python
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2
```

##### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$。
- **空间复杂度**：$O(1)$。


理解了上面这道题的题意，就可以试着自己编写代码，并尝试提交通过。如果提交结果显示「通过」，那么恭喜你完成了 LeetCode 上的第一题。虽然只是一道题，但这意味着刷题计划的开始！希望你能坚持下去，得到应有的收获。

## 3. LeetCode 刷题攻略

### 3.1 LeetCode 前期准备

如果你是算法和数据结构的新手，建议在刷 LeetCode 之前先学习一下基础知识，这样刷题时会更顺利。

基础知识包括：
- **数据结构**：数组、字符串、链表、树（如二叉树）等。
- **算法**：分治、贪心、回溯、动态规划等。

这个阶段推荐看一些经典的算法基础书来进行学习。这里推荐一下我看过的感觉不错的算法书：

- 【书籍】[算法（第 4 版）- 谢路云 译](https://book.douban.com/subject/19952400/)
- 【书籍】[大话数据结构 - 程杰 著](https://book.douban.com/subject/6424904/)
- 【书籍】[趣学算法 - 陈小玉 著](https://book.douban.com/subject/27109832/)
- 【书籍】[算法图解 - 袁国忠 译](https://book.douban.com/subject/26979890/)
- 【书籍】[算法竞赛入门经典（第 2 版） - 刘汝佳 著](https://book.douban.com/subject/25902102/)
- 【书籍】[数据结构与算法分析 - 冯舜玺 译](https://book.douban.com/subject/1139426/)
- 【书籍】[算法导论（原书第 3 版） - 殷建平 / 徐云 / 王刚 / 刘晓光 / 苏明 / 邹恒明 / 王宏志 译](https://book.douban.com/subject/20432061/)

当然，也可以直接看我写的「算法通关手册」，欢迎指正和提出建议，万分感谢。

- 「算法通关手册」GitHub 地址：[https://github.com/itcharge/AlgoNote](https://github.com/itcharge/AlgoNote)
- 「算法通关手册」电子书网站地址：[https://algo.itcharge.cn](https://algo.itcharge.cn)

### 3.2 LeetCode 刷题顺序

讲个笑话，从前有个人以为 LeetCode 的题目是按照难易程度排序的，所以他从 [1. 两数之和](https://leetcode.cn/problems/two-sum) 开始刷题，结果他卡在了 [4. 寻找两个正序数组的中位数](https://leetcode.cn/problems/median-of-two-sorted-arrays) 这道困难题上。

LeetCode 的题目序号并不是按难易程度排序的，不建议按序号顺序刷题。新手建议从「简单」难度开始，熟练后再刷中等难度题目，最后考虑面试题或难题。

其实 LeetCode 官方网站上就有整理好的题目不错的刷题清单。链接为：[https://leetcode.cn/leetbook/](https://leetcode.cn/leetbook/)。可以先刷这里边的题目卡片。我这里也做了一个整理。

推荐刷题顺序和目录如下：

[1. 初级算法](https://leetcode.cn/leetbook/detail/top-interview-questions-easy/)、[2. 数组类算法](https://leetcode.cn/leetbook/detail/all-about-array/)、[3. 数组和字符串](https://leetcode.cn/leetbook/detail/array-and-string/)、[4. 链表类算法](https://leetcode.cn/leetbook/detail/linked-list/)、[5. 哈希表](https://leetcode.cn/leetbook/detail/hash-table/)、[6. 队列 & 栈](https://leetcode.cn/leetbook/detail/queue-stack/)、[7. 递归](https://leetcode.cn/leetbook/detail/recursion/)、[8. 二分查找](https://leetcode.cn/leetbook/detail/binary-search/)、[9. 二叉树](https://leetcode.cn/leetbook/detail/data-structure-binary-tree/)、[10. 中级算法](https://leetcode.cn/leetbook/detail/top-interview-questions-medium/)、[11. 高级算法](https://leetcode.cn/leetbook/detail/top-interview-questions-hard/)、[12. 算法面试题汇总](https://leetcode.cn/leetbook/detail/top-interview-questions/)。

当然还可以通过官方推出的「[学习计划 - 力扣](https://leetcode.cn/study-plan/)」按计划每天刷题。

或者直接按照我整理的分类刷题列表进行刷题：

- LeetCode 分类刷题列表：[点击打开「LeetCode 分类刷题列表」](https://github.com/itcharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md)

正在准备面试、没有太多时间刷题的小伙伴，可以按照我总结的「LeetCode 面试最常考 100 题」、「LeetCode 面试最常考 200 题」进行刷题。

> **说明**：「LeetCode 面试最常考 100 题」、「LeetCode 面试最常考 200 题」是笔者根据「[CodeTop 企业题库](https://codetop.cc/home)」按频度从高到低进行筛选，并且去除了一部分 LeetCode 上没有的题目和重复题目后得到的题目清单。

- [LeetCode 面试最常考 100 题](https://github.com/itcharge/AlgoNote/tree/main/docs/00_preface/00_07_interview_100_list.md)
- [LeetCode 面试最常考 200 题](https://github.com/itcharge/AlgoNote/tree/main/docs/00_preface/00_08_interview_200_list.md)

### 3.3 LeetCode 刷题技巧

下面分享一下我在刷题过程中用到的刷题技巧。简单来说，可以分为 $5$ 条：

> 1. 五分钟思考法
> 2. 重复刷题
> 3. 按专题分类刷题
> 4. 写解题报告
> 5. 坚持刷题

#### 3.3.1 五分钟思考法

> **五分钟思考法**：如果一道题如果 $5$ 分钟之内有思路，就立即动手写代码解题。如果 $5$ 分钟之后还没有思路，就直接去看题解。然后根据题解的思路，自己去实现代码。如果发现自己看了题解也无法实现代码，就认真阅读题解的代码，并理解代码的逻辑。

其实，刷算法题的过程和背英语单词很相似。

刚开始学英语时，先从最基础的字母学起，不必纠结每个字母的由来。接着学习简单的单词，也不用深究单词的含义，先记住再说。掌握了基础词汇后，再逐步学习词组、短句、长句，最后阅读文章。

背单词不是看一遍就能记住，而是需要不断重复练习、反复记忆来加深印象。

刷算法题也是如此。零基础时，不要纠结为什么自己想不出解法，或者为什么没想到更高效的方法。遇到没有思路的题目时，直接去看题解区的高赞解答，尽快积累经验，帮助自己快速入门。

#### 3.3.2 重复刷题

> **重复刷题**：遇见不会的题，多刷几遍，不断加深理解。

刷算法题经常是做完一遍后，隔一段时间就忘记了，看到之前做过的题目也未必能立刻想起解题思路。所以，刷题并不是做完一遍就结束了，还需要定期回顾和复习。

此外，一道题往往有多种解法和不同的优化思路。第一次做时可能只想到一种方法，等到第二遍、第三遍时，可能会发现新的解法或更优的实现。

因此，建议对不会的题目多刷几遍，通过反复练习不断加深理解和记忆。

#### 3.3.3 按专题分类刷题

> **按专题分类刷题**：按照不同专题分类刷题，既可以巩固刚学完的算法知识，还可以提高刷题效率。

按专题分类刷题有两个好处：

1. **巩固知识**：刚学完某个算法时，可能对里边的相关知识理解的不够透彻，或者说可能会遗漏一些关键知识点，这时候可以通过刷对应题目的方式来帮助我们巩固刚学完的算法知识。
2. **提高效率**：同类题目所用到的算法知识其实是相同或者相似的，同一种解题思路可以运用到多道题目中。通过不断求解同一类算法专题下的题目，可以大大的提升我们的刷题速度。

####  3.3.4 写解题报告

> **写解题报告**：如果能够用简洁清晰的语言让别人听懂这道题目的思路，那就说明你真正理解了这道题的解法。

写解题报告是很有用的技巧。如果你能用通俗易懂的语言写出解题思路，说明你真正理解了这道题。这相当于「费曼学习法」，也能减少重复刷题的时间。

#### 3.3.5 坚持刷题

> **坚持刷题**：算法刷题没有捷径，只有不断的刷题、总结，再刷题，再总结。

千万不要相信「3天精通数据结构」这类速成学习宣传。学习算法需要不断积累，反复理解算法思想，并通过刷题来应用知识。

根据我的个人经验，能坚持每天刷题并掌握基础算法知识的人总是少数。但如果你选择了学习算法，希望在达成目标前能坚持下去，通过「刻意练习」把刷题变成兴趣。

## 4. 总结

LeetCode 是一个在线编程练习平台，主要用于提升算法和编程能力。新手可以从简单题目开始，逐步学习数据结构和算法。

刷题技巧包括：五分钟思考法、重复刷题、按专题分类刷题、写解题报告、坚持刷题。最重要的是坚持，通过不断练习和总结来掌握算法知识。

## 练习题目

- [2235. 两整数相加](https://github.com/itcharge/AlgoNote/tree/main/docs/solutions/2200-2299/add-two-integers.md)
- [1929. 数组串联](https://github.com/itcharge/AlgoNote/tree/main/docs/solutions/1900-1999/concatenation-of-array.md)

## 参考资料

- 【文章】[What is LeetCode? - Quora](https://www.quora.com/What-is-Leetcode)
- 【文章】[LeetCode 帮助中心 - 力扣（LeetCode）](https://support.leetcode-cn.com/hc/)
- 【回答】[刷 leetcode 使用 python 还是 c++？ - 知乎](https://www.zhihu.com/question/319448129)
- 【回答】[刷完 LeetCode 是什么水平？能拿到什么水平的 offer？ - 知乎](https://www.zhihu.com/question/32019460)-->
