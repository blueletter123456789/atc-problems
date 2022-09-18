package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var scan = bufio.NewScanner(os.Stdin)

const (
	initBufSize = 10000
	maxBufSize = 10000000
)

func init() {
	buf := make([]byte, initBufSize)
	scan.Buffer(buf, maxBufSize)
	scan.Split(bufio.ScanWords)
}

func main() {
	n := NumStdin()

	a := make([]int, n)
	for i := range a {
		a[i] = NumStdin()
	}

	sort.Slice(a, func(i, j int) bool { return a[i] < a[j] })
	que := New(n)
	for i := range a {
		que.Enqueue(a[i])
	}

	var ans int
	for len(que.data) > 1 {
		minN, maxN := que.Top(), que.Bottom()

		ans++
		
		que.Pop()
		t := maxN % minN
		if t == 0 {
			continue
		} else {
			que.EnqueueLeft(t)
		}
	}

	fmt.Println(ans)
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}

type Queue struct {
	data []int
	size int
}

func New(cap int) *Queue {
	return &Queue{
		data: make([]int, 0, cap),
		size: 0,
	}
}

func (q *Queue) IsEmpty() bool {
	return q.size == 0
}

func (q *Queue) Top() int {
	return q.data[0]
}

func (q *Queue) Bottom() int {
	return q.data[q.size-1]
}

func (q *Queue) Enqueue(val int) {
	q.data = append(q.data, val)
	q.size++
}

func (q *Queue) EnqueueLeft(val int) {
	q.data = append([]int{val}, q.data...)
	q.size++
}

func (q *Queue) Dequeue() bool {
	if q.IsEmpty() {
		return false
	}
	q.data = q.data[1:]
	q.size--
	return true
}

func (q *Queue) Pop() bool {
	if q.IsEmpty() {
		return false
	}
	q.size--
	q.data = q.data[:q.size]
	return true
}
