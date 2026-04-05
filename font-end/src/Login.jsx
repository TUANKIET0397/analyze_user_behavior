import { FaArrowRight } from "react-icons/fa";
function Login() {
  function handleLogin() {
    // Xử lý logic đăng nhập tại đây
  }
  return (      
    <>
      <div>
        <span className="w-100 text-3xl">
          Dự đoán hành vi mua hàng của người dùng
        </span>
      </div>
      {/* login */}
      <div className="bg-white h-100 w-100 rounded-md mt-10">
        <div className="text-center my-5 mx-15">
          <span className="text-3xl">Đăng nhập</span>
          <p className="text-gray-400">
            Đăng nhập để truy cập vào hệ thống AI dự đoán
          </p>
        </div>
        <div className="flex flex-col mx-6 gap-1">
          <label htmlFor="username">Tên người dùng</label>
          <input
            type="text"
            id="username"
            placeholder="Nhập tên tài khoản"
            className="bg-gray-100 py-1 mb-3 px-4"
          />
          <label htmlFor="password">Mật khẩu</label>
          <input
            type="password"
            id="password"
            placeholder="........"
            className="bg-gray-100 py-1 px-4"
            required
          />
          <button className="bg-mauve-600 text-white flex items-center gap-2 rounded-md p-2 justify-center mt-3 cursor-pointer">
            Đăng nhập
            <FaArrowRight />
          </button>
        </div>
      </div>
    </>
  );
}
export default Login;
