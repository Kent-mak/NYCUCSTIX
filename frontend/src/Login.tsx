import * as React from "react";
import NavBar from "./NavBar";

type InputFieldProps = {
  id: string;
  labelText: string;
  type?: string;
  className?: string;
  value: string;
  onChange: (value: string) => void;
};

const InputField: React.FC<InputFieldProps> = ({ id, labelText, type = "text", className, value, onChange }) => (
  <div>
    <label htmlFor={id} className="sr-only">{labelText}</label>
    <input 
      id={id}
      type={type} 
      placeholder={labelText} 
      className={`justify-center px-4 py-1.5 max-w-full text-xl font-medium leading-8 bg-white rounded-lg border border-solid border-neutral-200 text-ellipsis text-zinc-500 w-full ${className}`} 
      value ={value}
      onChange = {(e) => onChange(e.target.value)}
    />
  </div>
);

const Login: React.FC = () => {
  const [account, setAccount] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [errorMessage, setErrorMessage] = React.useState("");

  const handleAccountChange = (value: string) => {
    setAccount(value);
  };

  const handlePasswordChange = (value: string) => {
    setPassword(value); 
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("accountName", account);
    formData.append("password", password);

    try {
      const response = await fetch("http://localhost:8000/login", {
        method: 'POST',
        body: formData,
      });

      if (response.status === 200) {
        const result = await response.json();
        console.log("Login successful:", result);
        setErrorMessage(""); // Clear any previous error messages
        // Handle successful login (e.g., redirect to another page)
      } else if (response.status === 401) {
        const errorResult = await response.json();
        setErrorMessage("Invalid account name or password.");
        console.error("Login failed:", errorResult);
        // Handle login failure (e.g., show error message to the user)
      } else {
        setErrorMessage("An unexpected error occurred. Please try again later.");
        console.error("Unexpected response status:", response.status);
        // Handle other unexpected statuses
      }
    } catch (error) {
      setErrorMessage("Network error. Please check your connection.");
      console.error('Error:', error);
      // Handle network or other errors
    }
  };
  return (
    <div className="flex flex-col">
      <NavBar />
      <div className="flex-grow flex justify-center items-center px-16 py-20 bg-white">
        <main className="flex flex-col justify-center items-center p-20 bg-white max-md:px-5">
          <header>
            <h1 className="mt-60 text-2xl font-semibold tracking-tight leading-9 text-center text-black max-md:mt-10">登入</h1>
            <p className="mt-1 text-base leading-6 text-center text-black">請輸入帳號及密碼</p>
          </header>
          <form onSubmit={handleSubmit}>
            <section>
              <InputField id="account" labelText="account name" value={account} onChange={handleAccountChange} />
              <InputField id="password" labelText="password" type="password" className="mt-4" value={password} onChange={handlePasswordChange} />
            </section>
            {errorMessage && <p className="text-red-500 mt-4">{errorMessage}</p>}
            <button type="submit" className="justify-center items-center px-4 py-2 mt-4 max-w-full text-base font-medium leading-6 text-white bg-black rounded-lg w-full max-md:px-5">
              Sign in
            </button>
          </form>
          <div className="flex gap-2 justify-center mt-6 max-w-full w-full">
            <div className="flex-1 shrink-0 h-px bg-neutral-200" />
            <div className="flex-1 shrink-0 h-px bg-neutral-200" />
          </div>
        </main>
      </div>
    </div>
  );
}

export default Login;