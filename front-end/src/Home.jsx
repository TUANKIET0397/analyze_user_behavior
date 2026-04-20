import img from "./assets/avatar.jpg"
import Chart from "./Chart"
import ProductItem from "./components/ProductItem"
import { BiSolidLike } from "react-icons/bi"
import { FaCartShopping } from "react-icons/fa6"
import { useMemo, useState } from "react"
import { createPrediction, explainPrediction } from "./api/api"

function Home() {
    const [featureData, setFeatureData] = useState([])
    const [donutData, setDonutData] = useState([])

    const [isEditing, setIsEditing] = useState(false)
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState("")
    const [predictionResult, setPredictionResult] = useState(null)
    const [predictionId, setPredictionId] = useState(null)

    const [stats, setStats] = useState([
        {
            key: "age",
            label: "TUỔI",
            value: "32",
            type: "text",
            inputType: "number",
        },
        {
            key: "gender",
            label: "GIỚI TÍNH",
            value: "Female",
            type: "select",
            options: ["Female", "Male"],
        },
        {
            key: "purchase_amount_usd",
            label: "SỐ TIỀN MUA HÀNG",
            value: "45",
            type: "text",
            inputType: "number",
        },
        {
            key: "previous_purchases",
            label: "TỔNG SỐ ĐƠN HÀNG",
            value: "128",
            type: "text",
            inputType: "number",
        },
        {
            key: "season",
            label: "MÙA",
            value: "Spring",
            type: "select",
            options: ["Fall", "Summer", "Spring", "Winter"],
        },
        {
            key: "subscription_status",
            label: "ĐĂNG KÍ THÀNH VIÊN",
            value: "Yes",
            type: "select",
            options: ["Yes", "No"],
        },
        {
            key: "frequency_of_purchases",
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
        {
            key: "review_rating",
            label: "REVIEW RATING",
            value: "2.3",
            type: "text",
            inputType: "number",
            step: "0.1",
        },
    ])

    function toggleEdit() {
        setIsEditing((prev) => !prev)
    }

    function handleInputChange(index, newValue) {
        setStats((prev) =>
            prev.map((item, itemIndex) =>
                itemIndex === index ? { ...item, value: newValue } : item,
            ),
        )
    }

    function buildPayload() {
        const getValue = (key) =>
            stats.find((item) => item.key === key)?.value ?? ""

        return {
            age: Number(getValue("age")),
            gender: getValue("gender"),
            purchase_amount_usd: Number(getValue("purchase_amount_usd")),
            review_rating: Number(getValue("review_rating")),
            season: getValue("season"),
            previous_purchases: Number(getValue("previous_purchases")),
            frequency_of_purchases: getValue("frequency_of_purchases"),
            subscription_status: getValue("subscription_status"),
        }
    }

    async function handleSubmitForm(e) {
        e.preventDefault()
        setLoading(true)
        setError("")

        try {
            const payload = buildPayload()

            const data = await createPrediction(payload)
            setPredictionResult(data)
            setPredictionId(data?.data?.id ?? null)
            setIsEditing(false)
            const [resPredict, resExplain] = await Promise.all([
                createPrediction(payload),
                explainPrediction(payload),
            ])
            setFeatureData(resExplain.data.feature_importance)

            const top = resPredict.data.prediction.top_categories

            setDonutData(
                top.map((item) => ({
                    name: item.category,
                    value: Math.round(item.confidence * 100),
                })),
            )
        } catch (err) {
            setError(err.message || "Có lỗi xảy ra")
        } finally {
            setLoading(false)
        }
    }

    const predictedCategory =
        predictionResult?.data?.prediction?.predicted_category || "Quần áo"

    const predictionConfidence =
        predictionResult?.data?.prediction?.confidence || null

    const smartDescription = useMemo(() => {
        if (!predictionResult) {
            return `Chưa có dự đoán nào được tạo ra. Vui lòng điền thông tin và nhấn "Dự đoán" để xem kết quả.`
        }

        const input = predictionResult.data.input
        const prediction = predictionResult.data.prediction

        return `Object có xu hướng mua sắm vào mùa ${input.season}, với tần suất ${input.frequency_of_purchases}. AI dự đoán nhóm sản phẩm phù hợp nhất hiện tại là ${prediction.predicted_category} với độ tin cậy ${(prediction.confidence * 100).toFixed(2)}%.`
    }, [predictionResult])

    return (
        <div>
            {/* body */}
            <div className="flex flex-col bg-gray-200 gap-4 px-4 py-3">
                <div className="flex gap-6">
                    {/* left */}
                    <form onSubmit={handleSubmitForm}>
                        {/* profile */}
                        <div className="bg-white rounded-md px-5 pt-4 pb-10 flex flex-col gap-y-4">
                            <div className="flex justify-between">
                                <div className="flex items-center">
                                    <img
                                        src={img}
                                        alt=""
                                        className="rounded-md h-12 w-13"
                                    />
                                    <p className="flex flex-col ml-4 gap-y-2 w-[100px]">
                                        <span className="text-[19px] font-bold">
                                            Group 5
                                        </span>
                                        <span className="text-[15px] text-gray-400">
                                            Object
                                        </span>
                                    </p>
                                </div>

                                <div className="flex items-center gap-4 pl-40">
                                    <button
                                        type="button"
                                        className="rounded-2xl bg-gray-700 px-4 h-8 w-auto text-white cursor-pointer"
                                        onClick={toggleEdit}
                                    >
                                        {isEditing ? "Đóng" : "Sửa"}
                                    </button>
                                    <button
                                        type="submit"
                                        disabled={loading}
                                        className="rounded-2xl bg-gray-700 px-4 w-[100px] h-8 max-w-[100px] text-white cursor-pointer disabled:opacity-70"
                                    >
                                        {loading
                                            ? "Đang dự đoán..."
                                            : "Dự đoán"}
                                    </button>
                                </div>
                            </div>

                            {error && (
                                <div className="mt-4 rounded-md bg-red-50 px-3 py-2 text-xs text-red-600">
                                    {error}
                                </div>
                            )}

                            {/* status */}
                            <div>
                                <div className="flex flex-col">
                                    {stats.map((item, index) => (
                                        <div
                                            key={item.key}
                                            className="py-4 border-b border-gray-100 last:border-0"
                                        >
                                            <span className="block text-[16px] font-bold text-gray-500 uppercase tracking-wide">
                                                {item.label}
                                            </span>

                                            {isEditing ? (
                                                <div className="mt-2">
                                                    {item.type === "select" && (
                                                        <select
                                                            value={item.value}
                                                            onChange={(e) =>
                                                                handleInputChange(
                                                                    index,
                                                                    e.target
                                                                        .value,
                                                                )
                                                            }
                                                            className="block w-full text-[16px] border border-gray-300 rounded p-1"
                                                        >
                                                            {item.options.map(
                                                                (option) => (
                                                                    <option
                                                                        key={
                                                                            option
                                                                        }
                                                                        value={
                                                                            option
                                                                        }
                                                                    >
                                                                        {option}
                                                                    </option>
                                                                ),
                                                            )}
                                                        </select>
                                                    )}

                                                    {item.type === "text" && (
                                                        <input
                                                            type={
                                                                item.inputType ||
                                                                "text"
                                                            }
                                                            step={item.step}
                                                            value={item.value}
                                                            onChange={(e) =>
                                                                handleInputChange(
                                                                    index,
                                                                    e.target
                                                                        .value,
                                                                )
                                                            }
                                                            className="block w-full text-[14px] text-gray-800 border border-gray-300 rounded p-1"
                                                        />
                                                    )}
                                                </div>
                                            ) : (
                                                <span className="block text-[14px] text-gray-800 font-medium">
                                                    {item.value}
                                                </span>
                                            )}
                                        </div>
                                    ))}
                                </div>
                            </div>
                        </div>
                    </form>

                    {/* right */}
                    <div className="flex-1">
                        {/* chart */}
                        <div>
                            <Chart
                                donutData={donutData}
                                featureData={featureData}
                            />
                        </div>
                        {/* items */}
                        <ProductItem predictionId={predictionId} />
                    </div>
                </div>
                {/* conclusion */}
                <div className="bg-white flex flex-col px-4 pt-4 pb-4 rounded-md">
                    <span className="font-bold text-[20px]">
                        Xu hướng hành vi
                    </span>
                    <span className=" mt-1 text-[18px] text-gray-700">
                        {smartDescription}
                    </span>

                    {predictionResult && (
                        <div className="ml-2 mt-2 text-sm text-gray-700">
                            <div>
                                <span className="font-semibold text-[17px]">
                                    Danh mục dự đoán:
                                </span>{" "}
                                {predictedCategory}
                            </div>

                            {predictionConfidence !== null && (
                                <div className="mt-1">
                                    <span className="font-semibold text-[17px]">
                                        Độ tin cậy:
                                    </span>{" "}
                                    {(predictionConfidence * 100).toFixed(2)}%
                                </div>
                            )}

                            <div className="mt-1">
                                <span className="font-semibold text-[17px]">
                                    Thời gian tạo:
                                </span>{" "}
                                {predictionResult.data.created_at}
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </div>
    )
}

export default Home
