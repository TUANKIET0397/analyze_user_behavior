import { FaArrowRight } from "react-icons/fa";
function Login() {
  return (      
    <>
      <div>
        <span className="w-100 text-3xl">
          Predict User Shopping Behavior
        </span>
      </div>
      {/* login */}
      <div className="bg-white h-100 w-100 rounded-md mt-10">
        <div className="text-center my-5 mx-15">
          <span className="text-3xl">Login</span>
          <p className="text-gray-400">
            Sign in to access the AI prediction system
          </p>
        </div>
        <div className="flex flex-col mx-6 gap-1">
          <label htmlFor="username">Username</label>
          <input
            type="text"
            id="username"
            placeholder="Enter your username"
            className="bg-gray-100 py-1 mb-3 px-4"
          />
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            placeholder="........"
            className="bg-gray-100 py-1 px-4"
            required
          />
          <button className="bg-mauve-600 text-white flex items-center gap-2 rounded-md p-2 justify-center mt-3 cursor-pointer">
            Login
            <FaArrowRight />
          </button>
        </div>
      </div>
    </>
  );
}
export default Login;
