import img from './assets/avatar.jpg';
function Home() {
  return (
    <div >
        <div className='flex justify-between px-5 py-2 items-center bg-gray-400'>
            <span>Bảng điều khiển</span>
            <img src={img} alt="avatar" className='rounded-full w-10 h-10'/>
        </div>
        {/* body */}
        <div className='grid grid-cols-3 bg-gray-200 h-screen'>
            {/* left */}
            <div className=''>
                <div className='flex justify-between items-center px-5 py-5'>
                    <div className='flex flex-col'>
                        <span className='text-xs'>CÁ NHÂN HÓA</span>
                        <span className='font-bold text-2xl'>Chỉnh sửa hồ sơ</span>
                    </div>
                    <button className='rounded-2xl bg-gray-700 px-4 h-8 text-white'>Sửa</button>
                </div>
                {/* profile */}
                <div className='mx-5 bg-white'>
                    <div className='flex'>
                        <img src={img} alt="" className='rounded-md h-12 w-12'/>
                        <div className='flex flex-col ml-5'>
                            <span className='font-bold'>Name</span>
                            <span>khách hàng</span>
                        </div>
                   </div>
                </div>
            </div>
            {/* right */}
            <div className='col-span-2'></div>
        </div>
    </div>
  );
}
export default Home;