import {
    PieChart,
    Pie,
    Cell,
    BarChart,
    Bar,
    XAxis,
    YAxis,
    ResponsiveContainer,
} from "recharts"

const donutColors = ["#666666", "#3b6dcc"]

export default function TwoCharts({ donutData, featureData }) {
    const sortedData = [...featureData].sort(
        (a, b) => b.impact_percent - a.impact_percent,
    )
    return (
        <div className="grid grid-cols-1 gap-6 md:grid-cols-2 mb-3 h-[400px]">
            {/* Donut chart */}
            <div className="rounded-md bg-white p-6 shadow-sm">
                <h2 className="mb-8 text-[18px] font-semibold uppercase tracking-wide text-gray-500">
                    Sản phẩm gợi ý
                </h2>

                <div className="relative h-65 w-full">
                    <ResponsiveContainer width="100%" height="100%">
                        <PieChart>
                            <Pie
                                data={donutData}
                                dataKey="value"
                                nameKey="name"
                                outerRadius={100}
                                stroke="none"
                                label={({ percent }) =>
                                    `${(percent * 100).toFixed(0)}%`
                                }
                            >
                                {donutData?.map((entry, index) => (
                                    <Cell
                                        key={`cell-${index}`}
                                        fill={
                                            donutColors[
                                                index % donutColors.length
                                            ]
                                        }
                                    />
                                ))}
                            </Pie>
                        </PieChart>
                    </ResponsiveContainer>
                </div>

                <div className="mt-4 flex justify-center gap-10 text-sm text-gray-700">
                    {donutData?.map((item, index) => (
                        <div key={index} className="flex items-center gap-3">
                            <span
                                className="h-3 w-3 rounded-full"
                                style={{
                                    background:
                                        donutColors[index % donutColors.length],
                                }}
                            />
                            <span>{item.name}</span>
                        </div>
                    ))}
                </div>
            </div>

            {/* Bar chart */}
            <div className="rounded-md bg-white p-6 shadow-sm">
                <h2 className="mb-8 text-[18px] font-semibold uppercase tracking-wide text-gray-500">
                    Các yếu tố ảnh hưởng
                </h2>

                <div className="h-65 w-full">
                    <ResponsiveContainer width="100%" height="100%">
                        <BarChart
                            data={sortedData}
                            layout="vertical"
                            margin={{ right: 60 }}
                        >
                            <XAxis type="number" hide />

                            <YAxis
                                dataKey="feature"
                                type="category"
                                width={120}
                                axisLine={false}
                                tickLine={false}
                                tick={{ fill: "#666", fontSize: 12 }}
                                tickFormatter={
                                    (val) => val.replaceAll("_", " ") // thay dấu gạch dưới bằng dấu cách
                                }
                            />

                            <Bar
                                dataKey="impact_percent"
                                radius={[0, 6, 6, 0]}
                                label={{ position: "right" }}
                            >
                                {sortedData.map((entry, index) => (
                                    <Cell
                                        key={`bar-${index}`}
                                        fill={
                                            index === 0
                                                ? "#3b6dcc"
                                                : index === 1
                                                  ? "#7da6ff"
                                                  : "#d9dbdf"
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
