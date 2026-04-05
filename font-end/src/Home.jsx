import img from "./assets/avatar.jpg";
import Chart from "./Chart";
import { BiSolidLike } from "react-icons/bi";
import { FaCartShopping } from "react-icons/fa6";
function Home() {
  const user = {
    name: "Baozeus",
  };
  const stats = [
    { label: "TUỔI", value: "32" },
    { label: "GIỚI TÍNH", value: "Nam" },
    { label: "THU NHẬP", value: "45M" },
    { label: "TỔNG SỐ ĐƠN HÀNG", value: "128" },
    { label: "QUẦN CỤT", value: "134" },
    { label: "ÁO THUN", value: "15" },
    { label: "QUẦN DÀI", value: "252" },
    { label: "DÂY NỊT", value: "23" },
    { label: "SỐ LƯỢNG ĐƠN", value: "421" },
    { label: "ĐƠN VÀO MÙA XUÂN", value: "200" },
    { label: "ĐƠN VÀO MÙA ĐÔNG", value: "221" },
    { label: "PHỤ KIỆN", value: "23" },
    { label: "THỜI TRANG", value: "23" },
  ];
  return (
    <div>
      <div className="flex justify-between px-5 py-2 items-center bg-gray-400">
        <span>Bảng điều khiển</span>
        <img src={img} alt="avatar" className="rounded-full w-10 h-10" />
      </div>
      {/* body */}
      <div className="grid grid-cols-3 bg-gray-200 ">
        {/* left */}
        <div className="">
          <div className="flex justify-between items-center px-5 py-5">
            <div className="flex flex-col">
              <span className="text-xs">CÁ NHÂN HÓA</span>
              <span className="font-bold text-2xl">Chỉnh sửa hồ sơ</span>
            </div>
            <button className="rounded-2xl bg-gray-700 px-4 h-8 text-white">
              Sửa
            </button>
          </div>
          {/* profile */}
          <div className=" bg-white px-5 py-5 mx-3 rounded-md">
            <div className="flex">
              <img src={img} alt="" className="rounded-md h-12 w-13" />
              <div className="flex flex-col ml-5 gap-y-2">
                <span className="font-bold">Name</span>
                <span className="text-xs text-gray-400">khách hàng</span>
              </div>
            </div>
            {/* status */}
            <div>
              <div className="flex flex-col">
                {stats.map((item, index) => (
                  <div
                    key={index}
                    className="py-4 border-b border-gray-100 last:border-0"
                  >
                    <span className="block text-xs font-bold text-gray-500 uppercase tracking-wide">
                      {item.label}
                    </span>
                    <span className="block text-xs text-gray-800 mt-2">
                      {item.value}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
        {/* right */}
        <div className="col-span-2 pl-20 pr-5">
          <div className="flex flex-col px-5 py-5">
            <span className="text-xs text-gray-400">Dữ liệu thông minh</span>
            <span className="font-bold text-2xl">Phân tích & Dự báo AI</span>
          </div>
          <div className="bg-white flex flex-col px-5 py-2 rounded-md">
            <span className="font-bold">Xu hướng hành vi</span>
            <span>
              Người dùng <span className="font-bold">{user.name}</span> có xu
              hướng chi tiêu mạnh vào cuối tuần, tập trung vào các mặt hàng Quần
              áo. Dự báo chi tiêu sẽ tăng 15% trong tháng tới do nhu cầu nâng
              cấp thiết bị cá nhân.
            </span>
          </div>
          {/* chart */}
          <div>
            <Chart />
          </div>
          <div className="flex gap-3 items-center my-5">
            <BiSolidLike size={32} color="blue" />
            <span className="text-2xl">Gợi ý mua sắm AI</span>
          </div>
          {/* items */}
          <div className="flex gap-2">
            <div className="w-75 rounded-2xl bg-[#f5f6fa] p-3 shadow-sm">
              <div className="relative">
                <img
                  src={img}
                  alt="Áo khoác"
                  className="h-45 w-full rounded-xl object-cover"
                />
  
                <div className="absolute right-3 top-3 rounded-full bg-blue-100 px-3 py-1 text-sm font-semibold text-blue-600">
                  Gợi ý 98%
                </div>
              </div>
              <div className="mt-4 px-2 pb-2">
                <p className="text-sm text-gray-400 uppercase">Áo</p>
  
                <h3 className="mt-1 text-xl font-semibold text-gray-800">Áo khoác</h3>
  
                <div className="mt-4 flex items-center justify-between">
                  <span className="text-lg font-bold text-gray-800">14.500.000đ</span>
  
                  <button className="flex h-10 w-10 items-center justify-center rounded-full bg-gray-200 hover:bg-gray-300">
                    <FaCartShopping size={20} color="gray" />
                  </button>
                </div>
              </div>
            </div>
            <div className="w-75 rounded-2xl bg-[#f5f6fa] p-3 shadow-sm">
              <div className="relative">
                <img
                  src={img}
                  alt="Áo khoác"
                  className="h-45 w-full rounded-xl object-cover"
                />
  
                <div className="absolute right-3 top-3 rounded-full bg-blue-100 px-3 py-1 text-sm font-semibold text-blue-600">
                  Gợi ý 98%
                </div>
              </div>
              <div className="mt-4 px-2 pb-2">
                <p className="text-sm text-gray-400 uppercase">Áo</p>
  
                <h3 className="mt-1 text-xl font-semibold text-gray-800">Áo khoác</h3>
  
                <div className="mt-4 flex items-center justify-between">
                  <span className="text-lg font-bold text-gray-800">14.500.000đ</span>
  
                  <button className="flex h-10 w-10 items-center justify-center rounded-full bg-gray-200 hover:bg-gray-300">
                    <FaCartShopping size={20} color="gray" />
                  </button>
                </div>
              </div>
            </div>
            <div className="w-75 rounded-2xl bg-[#f5f6fa] p-3 shadow-sm">
              <div className="relative">
                <img
                  src={img}
                  alt="Áo khoác"
                  className="h-45 w-full rounded-xl object-cover"
                />
  
                <div className="absolute right-3 top-3 rounded-full bg-blue-100 px-3 py-1 text-sm font-semibold text-blue-600">
                  Gợi ý 98%
                </div>
              </div>
              <div className="mt-4 px-2 pb-2">
                <p className="text-sm text-gray-400 uppercase">Áo</p>
  
                <h3 className="mt-1 text-xl font-semibold text-gray-800">Áo khoác</h3>
  
                <div className="mt-4 flex items-center justify-between">
                  <span className="text-lg font-bold text-gray-800">14.500.000đ</span>
  
                  <button className="flex h-10 w-10 items-center justify-center rounded-full bg-gray-200 hover:bg-gray-300">
                    <FaCartShopping size={20} color="gray" />
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
export default Home;
