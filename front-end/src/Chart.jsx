import {
    PieChart,
    Pie,
    Cell,
    BarChart,
    Bar,
    XAxis,
    ResponsiveContainer,
} from "recharts"

const donutData = [
    { name: "Footwear", value: 52 },
    { name: "Phụ kiện", value: 28 },
]

const donutColors = ["#666666", "#3b6dcc"]

const trendData = [
    { month: "THÁNG 1", value: 32 },
    { month: "", value: 48 },
    { month: "", value: 38 },
    { month: "", value: 62 },
    { month: "", value: 75 },
    { month: "THÁNG 6", value: 55 },
]

export default function TwoCharts() {
    return (
        <div className="grid grid-cols-1 gap-6 md:grid-cols-2 mt-4">
            {/* Donut chart */}
            <div className="rounded-md bg-white p-6 shadow-sm">
                <h2 className="mb-8 text-[18px] font-semibold uppercase tracking-wide text-gray-500">
                    Cơ cấu chi tiêu
                </h2>

                <div className="relative h-65 w-full">
                    <ResponsiveContainer width="100%" height="100%">
                        <PieChart>
                            <Pie
                                data={donutData}
                                dataKey="value"
                                nameKey="name"
                                innerRadius={75}
                                outerRadius={100}
                                paddingAngle={1}
                                stroke="none"
                            >
                                {donutData.map((entry, index) => (
                                    <Cell
                                        key={`cell-${index}`}
                                        fill={donutColors[index]}
                                    />
                                ))}
                            </Pie>
                        </PieChart>
                    </ResponsiveContainer>

                    <div className="pointer-events-none absolute inset-0 flex flex-col items-center justify-center">
                        <div className="text-4xl font-bold text-gray-800">
                            120M
                        </div>
                        <div className="mt-1 text-sm uppercase tracking-wide text-gray-400">
                            Tổng chi
                        </div>
                    </div>
                </div>

                <div className="mt-4 flex justify-center gap-10 text-sm text-gray-700">
                    <div className="flex items-center gap-3">
                        <span className="h-3 w-3 rounded-full bg-[#666666]" />
                        <span>Footwear</span>
                    </div>
                    <div className="flex items-center gap-3">
                        <span className="h-3 w-3 rounded-full bg-[#3b6dcc]" />
                        <span>Phụ kiện</span>
                    </div>
                </div>
            </div>

            {/* Bar chart */}
            <div className="rounded-md bg-white p-6 shadow-sm">
                <h2 className="mb-8 text-[18px] font-semibold uppercase tracking-wide text-gray-500">
                    Biểu đồ xu hướng (6 tháng)
                </h2>

                <div className="h-65 w-full">
                    <ResponsiveContainer width="100%" height="100%">
                        <BarChart data={trendData} barCategoryGap="18%">
                            <XAxis
                                dataKey="month"
                                axisLine={false}
                                tickLine={false}
                                interval={0}
                                tick={{ fill: "#666", fontSize: 12 }}
                            />
                            <Bar dataKey="value" radius={[4, 4, 0, 0]}>
                                {trendData.map((entry, index) => (
                                    <Cell
                                        key={`bar-${index}`}
                                        fill={
                                            index === 4 ? "#666666" : "#d9dbdf"
                                        }
                                    />
                                ))}
                            </Bar>
                        </BarChart>
                    </ResponsiveContainer>
                </div>
            </div>
        </div>
    )
}
