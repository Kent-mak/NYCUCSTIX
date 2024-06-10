import * as React from "react";
import NavBar from "./NavBar";

type InputFieldProps = {
  id: string;
  labelText: string;
  type?: string;
  className?: string;
};

const InputField: React.FC<InputFieldProps> = ({ id, labelText, type = "text", className }) => (
  <div>
    <label htmlFor={id} className="sr-only">{labelText}</label>
    <input id={id} type={type} placeholder={labelText} className={`justify-center px-4 py-1.5 max-w-full text-xl font-medium leading-8 bg-white rounded-lg border border-solid border-neutral-200 text-ellipsis text-zinc-500 w-full ${className}`} />
  </div>
);

const Login: React.FC = () => {
  return (
    <div className="flex flex-col">
      <NavBar />
      <div className="flex-grow flex justify-center items-center px-16 py-20 bg-white">
        <main className="flex flex-col justify-center items-center p-20 bg-white max-md:px-5">
          <header>
            <h1 className="mt-60 text-2xl font-semibold tracking-tight leading-9 text-center text-black max-md:mt-10">登入</h1>
            <p className="mt-1 text-base leading-6 text-center text-black">請輸入帳號及密碼</p>
          </header>
          <form>
            <section>
              <InputField id="accountName" labelText="account name" />
              <InputField id="password" labelText="password" type="password" className="mt-4" />
            </section>
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