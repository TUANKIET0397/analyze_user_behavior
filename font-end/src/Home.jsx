import img from "./assets/avatar.jpg";
import Chart from "./Chart";
import { BiSolidLike } from "react-icons/bi";
import { FaCartShopping } from "react-icons/fa6";
import { useState } from "react";
function Home() {
  const [isEditing, setIsEditing] = useState(false);
  function toggleEdit() {
    setIsEditing(!isEditing);
  }
  function handleInputChange(index, newValue) {
    const newStats = [...stats];
    newStats[index].value = newValue;
    setStats(newStats);
  }
  const user = {
    name: "Baozeus",
  };
  const [stats, setStats] = useState([
    { label: "TUỔI", value: "32", type: "text" },
    { label: "GIỚI TÍNH", value: "Nam", type: "text" },
    { label: "SỐ TIỀN MUA HÀNG", value: "45M", type: "text" },
    { label: "TỔNG SỐ ĐƠN HÀNG", value: "128", type: "text" },
    {
      label: "MÙA",
      value: "Mùa Xuân",
      type: "select",
      options: ["Fall", "Summer", "Spring", "Winter"],
    },
    { label: "ĐĂNG KÍ THÀNH VIÊN", value: "Đã Đăng Kí", type: "boolean" },
    {
      label: "TẦN SUẤT MUA HÀNG",
      value: "bi-weekly",
      type: "select",
      options: [
        "weekly",
        "bi-weekly",
        "fortnightly",
        "monthly",
        "every 3 months",
        "quarterly",
        "annually",
      ],
    },
    { label: "REVIEW RATING", value: "2.3", type: "text" },
  ]);

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
            <div className="flex gap-3">
              <button className="rounded-2xl bg-gray-700 px-4 h-8 text-white cursor-pointer">
                Dự đoán
              </button>
              <button
                className="rounded-2xl bg-gray-700 px-4 h-8 text-white cursor-pointer"
                onClick={toggleEdit}
              >
                {isEditing ? "Lưu" : "Sửa"}
              </button>
            </div>
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
                    {isEditing ? (
                      <div className="mt-2">
                        {/* trường hợp select */}
                        {item.type === "select" && (
                          <select
                            value={item.value}
                            onChange={(e) =>
                              handleInputChange(index, e.target.value)
                            }
                            className="
                            block
                            w-full
                            text-xs
                            border
                            border-gray-300
                            rounded
                            p-1"
                          >
                            {item.options.map((option, index) => (
                              <option key={index} value={option}>
                                {option}
                              </option>
                            ))}
                          </select>
                        )}
                        {/* trường hợp boolean */}
                        {item.type === "boolean" && (
                          <label className="flex items-center cursor-pointer">
                            <input
                              type="checkbox"
                              checked={item.value}
                              onChange={(e) =>
                                handleInputChange(index, e.target.checked)
                              }
                              className="mr-2"
                            />
                            <span className="text-xs text-gray-600">
                              Kích hoạt
                            </span>
                          </label>
                        )}
                        {/* trường hợp text */}
                        {item.type === "text" && (
                          <input
                            type="text"
                            value={item.value}
                            onChange={(e) => {
                              handleInputChange(index, e.target.value);
                            }}
                            className="block text-xs text-gray-800 mt-2"
                          />
                        )}
                      </div>
                    ) : (
                      <span className="block text-xs text-gray-800 mt-2 font-medium">
                        {item.label === "ĐĂNG KÍ THÀNH VIÊN"
                          ? item.value
                            ? "Đã đăng ký"
                            : "Chưa đăng ký"
                          : item.value}
                      </span>
                    )}
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

                <h3 className="mt-1 text-xl font-semibold text-gray-800">
                  Áo khoác
                </h3>

                <div className="mt-4 flex items-center justify-between">
                  <span className="text-lg font-bold text-gray-800">
                    14.500.000đ
                  </span>

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

                <h3 className="mt-1 text-xl font-semibold text-gray-800">
                  Áo khoác
                </h3>

                <div className="mt-4 flex items-center justify-between">
                  <span className="text-lg font-bold text-gray-800">
                    14.500.000đ
                  </span>

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

                <h3 className="mt-1 text-xl font-semibold text-gray-800">
                  Áo khoác
                </h3>

                <div className="mt-4 flex items-center justify-between">
                  <span className="text-lg font-bold text-gray-800">
                    14.500.000đ
                  </span>

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
