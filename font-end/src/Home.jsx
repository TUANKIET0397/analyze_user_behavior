import img from "./assets/avatar.jpg";
function Home() {
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
      <div className="grid grid-cols-3 bg-gray-200 h-screen">
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
        <div className="col-span-2"></div>
      </div>
    </div>
  );
}
export default Home;
