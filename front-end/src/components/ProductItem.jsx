import { useEffect, useState } from "react"
import { FaCartShopping } from "react-icons/fa6"

const API_URL = import.meta.env.VITE_API_BACKEND

export default function ProductItem({ predictionId }) {
    const [products, setProducts] = useState([])

    useEffect(() => {
        if (!predictionId) {
            console.warn("No prediction ID provided, skipping product fetch.")
            return
        }

        fetch(`${API_URL}/api/predictions/${predictionId}/products`)
            .then((res) => res.json())
            .then((res) => {
                setProducts(res?.data?.products || [])
            })
            .catch(console.error)
    }, [predictionId])
    if (!products.length) {
        return null
    }

    return (
        <div className="flex gap-3 overflow-x-auto py-3">
            {products.map((item) => (
                <div
                    key={item.id}
                    className="w-75 rounded-2xl bg-[#f5f6fa] p-3 shadow-sm"
                >
                    <div className="relative">
                        <img
                            src={`${API_URL}/${item.image_path || ""}`}
                            alt={item.product_name}
                            className="h-45 w-full rounded-xl object-cover"
                        />

                        <div className="absolute right-3 top-3 rounded-full bg-blue-100 px-3 py-1 text-sm font-semibold text-blue-600">
                            Gợi ý
                        </div>
                    </div>

                    <div className="mt-4 px-2 pb-2">
                        <p className="text-sm text-gray-400 uppercase">
                            {item.category}
                        </p>

                        <h3 className="mt-1 text-xl font-semibold text-gray-800">
                            {item.product_name}
                        </h3>

                        <div className="mt-4 flex items-center justify-between">
                            <span className="text-lg font-bold text-gray-800">
                                {item.price.toLocaleString()} $
                            </span>

                            <button
                                type="button"
                                className="flex h-10 w-10 items-center justify-center rounded-full bg-gray-200 hover:bg-gray-300"
                            >
                                <FaCartShopping size={20} color="gray" />
                            </button>
                        </div>
                    </div>
                </div>
            ))}
        </div>
    )
}
