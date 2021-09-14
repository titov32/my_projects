fn main() {
    println!("Печать чисел фиббоначи с помощью рекурсии");
    fn fib(num: u128) -> u128 {
        if num == 0 {
            0
        } else if num == 1 {
            1
        } else {
            fib(num - 1) + fib(num - 2)
        }
    }

    for num in 1..43 {
        let a = fib(num);
        println!("fib {} = {}", num, a);
    }
}
