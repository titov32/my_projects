use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]

fn fib(num: u128) -> u128 {
        if num == 0 {
            0
        } else if num == 1 {
            1
        } else {
            fib(num - 1) + fib(num - 2)
        }
    }

    

#[pymodule]
/// A Python module implemented in Rust.
fn rustfib(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(fib))?;

    Ok(())
}