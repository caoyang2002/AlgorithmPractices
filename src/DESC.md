查看原作者更新文档： https://algo.itcharge.cn/

> [!NOTE]
>
> fsa

# 数学

```markdown
文本文本\\( \int x dx = \frac{x^2}{2} + C \\)文本文本
```

文本文本\\( \int x dx = \frac{x^2}{2} + C \\)文本文本

```markdown
文本文本\\[ \mu = \frac{1}{N} \sum_{i=0} x_i \\]文本文本
```

文本文本\\[ \mu = \frac{1}{N} \sum_{i=0} x_i \\]文本文本

```markdown
文本文本$$ a = \frac{x^2}{2} \times C $$文本文本
```

文本文本$$ a = \frac{x^2}{2} \times C $$文本文本

```markdown
文本文本$fs$文本文本
```

文本文本$fs$文本文本


https://mdbook-guide.irust.net/zh-cn/format/mdbook.html

# 预处理命令

```bash
Shell
Bash script
Batch script
Python3
Node
Rust
```

```rust
fn main() {
    println!("Hello from rust");
}
```
# make
```bash
cmdrun cd tests/cpp && cmake -G Ninja ./ && ninja && call main.exe
```

# python 输出

```bash
cmdrun python3 tests/test.py
```

<!-- cmdrun python3 tests/test.py -->

---

# bash 输出

```bash
cmdrun bash tests/run_c.sh
```

<!-- cmdrun bash tests/run_c.sh -->

---

# Batch 输出

```bash
cmdrun call tests/win.bat
```

<!-- cmdrun call tests/win.bat -->

---

# shell 输出

```bash
cmdrun echo hello; echo world;
```
<!-- cmdrun echo oui; echo non; -->

```bash
cmdrun yes 42 | head -n 10 | sed -z 's/\n/  \n/g'
```

<!-- cmdrun yes 42 | head -n 10 | sed -z 's/\n/  \n/g' -->

```bash
cmdrun seq 1 10 | tail -n 5 | rev
```

<!-- cmdrun seq 1 10 | tail -n 5 | rev -->

---

# node

```bash
cmdrun node tests/node.mjs apples
```

<!-- cmdrun node tests/node.mjs apples  -->

```bash
cmdrun node tests/node.mjs bananas
```

<!-- cmdrun node tests/node.mjs bananas -->



---

# rust

```bash
<!-- cmdrun rustc tests/rust.rs && call rust.exe && del rust.exe && del rust.pdb -->
```

<!-- cmdrun rustc tests/rust.rs && call rust.exe && del rust.exe && del rust.pdb -->

```bash
cmdrun rustc tests/rust.rs && rm -f ./rust
```
<!-- cmdrun rustc tests/rust.rs && ./rust && rm -f ./rust -->

---

# c lang

## windows
```bash
cmdrun g++ tests/cpp/main.cpp -o c && call c.exe && del c.exe
```

<!-- cmdrun g++ tests/cpp/main.cpp -o c && call c.exe && del c.exe-->

# mac

```bash
cmdrun g++ tests/cpp/main.cpp -o c && tests/c && rm -f ./c
```

<!-- cmdrun g++ tests/cpp/main.cpp -o c && ./c && rm -f ./c -->

# bash 输出

```bash
cmdrun echo hello && echo world
```

<!-- cmdrun echo hello && echo world -->

```bash
cmdrun yes 42 | head -n 10 | sed -z 's/\n/  \n/g'
```

<!-- cmdrun yes 42 | head -n 10 | sed -z 's/\n/  \n/g' -->

```bash
cmdrun seq 1 10 | tail -n 5
```

<!-- cmdrun seq 1 10 | tail -n 5 -->


---



# other

```bash
cmdrun -0 echo hello world
```

<!-- cmdrun -0 echo hello world -->

```bash
cmdrun --0 echo hello world
```

<!-- cmdrun --0 echo hello world -->



```diff
<!-- cmdrun -0 diff tests/a.py tests/b.py -->
```

```diff
<!-- cmdrun -1 diff tests/a.py tests/b.py -->
```

```bash
<!-- cmdrun ls -->
```
