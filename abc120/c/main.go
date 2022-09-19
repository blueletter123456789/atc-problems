package main

import (
	"bufio"
	"fmt"
	"os"
)

var scan = bufio.NewScanner(os.Stdin)

const (
	initBufSize = 10000
	maxBufSize = 10000000
)

type Stack struct {
	data []string
	size int
}

func New(n int) *Stack {
	return &Stack{
		make([]string, 0, n),
		0,
	}
}

func (s *Stack) IsEmpty() bool {
	return s.size == 0
}

func (s *Stack) Push(x string) {
	s.size++
	s.data = append(s.data, x)
}

func (s *Stack) Pop() bool {
	if s.size == 0 {
		return false
	}
	s.size--
	s.data = s.data[:s.size]
	return true
}

func (s *Stack) Bottom() string {
	return s.data[s.size-1]
}

func init() {
	buf := make([]byte, initBufSize)
	scan.Buffer(buf, maxBufSize)
	scan.Split(bufio.ScanWords)
}

func main() {
	s := StrStdin()
	stack := New(len(s))

	var ans int
	for _, chr := range s {
		if stack.IsEmpty() {
			stack.Push(string(chr))
			continue
		}

		if stack.Bottom() != string(chr) {
			stack.Pop()
			ans += 2
		} else {
			stack.Push(string(chr))
		}
	}

	fmt.Println(ans)

	// explanation
	// The number of operations is min(number of 0's, number of 1's)*2
}

func StrStdin() string {
	scan.Scan()
	return scan.Text()
}
