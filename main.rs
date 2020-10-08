fn main(){
    let mut fizzbuzz = String::from("");
    for i in 1..100{
        if i % 3 == 0{
            fizzbuzz.push_str("fizz");
        }
        if i % 5 == 0{
            fizzbuzz.push_str("buzz");
        }
        if fizzbuzz == ""{
            fizzbuzz = i.to_string();
        }
        println!("{}", fizzbuzz);
        fizzbuzz.clear();
    }
}
