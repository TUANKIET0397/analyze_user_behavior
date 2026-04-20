function SkeletonBlock({ className = "" }) {
    return (
        <div className={`animate-pulse rounded-md bg-gray-200 ${className}`} />
    )
}

function TwoChartsSkeleton() {
    return (
        <div className="grid grid-cols-1 gap-6 md:grid-cols-2 mb-3 h-[400px]">
            {/* Donut skeleton */}
            <div className="rounded-md bg-white p-6 shadow-sm">
                <SkeletonBlock className="mb-8 h-6 w-40" />

                <div className="relative h-65 w-full flex items-center justify-center">
                    <div className="relative h-52 w-52 animate-pulse rounded-full bg-gray-200">
                        <div className="absolute inset-10 rounded-full bg-white" />
                    </div>
                </div>

                <div className="mt-4 flex justify-center gap-10 text-sm">
                    <div className="flex items-center gap-3">
                        <SkeletonBlock className="h-3 w-3 rounded-full" />
                        <SkeletonBlock className="h-4 w-20" />
                    </div>
                    <div className="flex items-center gap-3">
                        <SkeletonBlock className="h-3 w-3 rounded-full" />
                        <SkeletonBlock className="h-4 w-24" />
                    </div>
                </div>
            </div>

            {/* Bar skeleton */}
            <div className="rounded-md bg-white p-6 shadow-sm">
                <SkeletonBlock className="mb-8 h-6 w-48" />

                <div className="h-65 w-full flex flex-col justify-center gap-4">
                    {[1, 2, 3, 4, 5].map((item, index) => (
                        <div key={item} className="flex items-center gap-4">
                            <SkeletonBlock className="h-4 w-24" />
                            <SkeletonBlock
                                className={`h-6 rounded-r-md ${
                                    index === 0
                                        ? "w-40"
                                        : index === 1
                                          ? "w-32"
                                          : index === 2
                                            ? "w-28"
                                            : index === 3
                                              ? "w-24"
                                              : "w-20"
                                }`}
                            />
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}

import Skeleton from "react-loading-skeleton"
import "react-loading-skeleton/dist/skeleton.css"

function ProductSkeleton() {
    return (
        <div className="flex gap-3 overflow-x-auto py-3">
            {[1, 2, 3].map((item) => (
                <div
                    key={item}
                    className="w-75 rounded-2xl bg-[#f5f6fa] p-3 shadow-sm"
                >
                    <div className="relative">
                        <Skeleton height={180} borderRadius={16} />
                        <div className="absolute right-3 top-3">
                            <Skeleton
                                height={28}
                                width={60}
                                borderRadius={999}
                            />
                        </div>
                    </div>

                    <div className="mt-4 px-2 pb-2">
                        <Skeleton height={14} width={70} />
                        <div className="mt-2">
                            <Skeleton height={24} width={160} />
                        </div>

                        <div className="mt-4 flex items-center justify-between">
                            <Skeleton height={24} width={90} />
                            <Skeleton circle height={40} width={40} />
                        </div>
                    </div>
                </div>
            ))}
        </div>
    )
}

export { TwoChartsSkeleton, ProductSkeleton, SkeletonBlock }
