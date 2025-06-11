import React, { useEffect, useRef } from "react";
import * as d3 from "d3";

type DataItem = {
  name: string;
  total_quantity: number;
};

type Props = {
  data: DataItem[];
};

const D3plot: React.FC<Props> = ({ data }) => {

    
    const svgRef = useRef<SVGSVGElement | null>(null);

  useEffect(() => {
    if (!svgRef.current || data.length === 0) return;

    const svg = d3.select(svgRef.current);
    const width = 600;
    const height = 300;
    svg.selectAll("*").remove(); // 清空旧图

    svg.attr("width", width).attr("height", height);

    const margin = { top: 20, right: 20, bottom: 40, left: 50 };
    const innerWidth = width - margin.left - margin.right;
    const innerHeight = height - margin.top - margin.bottom;

    const g = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);

    const x = d3.scaleBand()
      .domain(data.map(d => d.name))
      .range([0, innerWidth])
      .padding(0.2);

    const y = d3.scaleLinear()
      .domain([0, d3.max(data, d => d.total_quantity)!])
      .nice()
      .range([innerHeight, 0]);

    g.append("g")
      .call(d3.axisLeft(y));

    g.append("g")
      .attr("transform", `translate(0,${innerHeight})`)
      .call(d3.axisBottom(x));

    g.selectAll("rect")
      .data(data)
      .enter()
      .append("rect")
      .attr("x", d => x(d.name)!)
      .attr("y", d => y(d.total_quantity))
      .attr("width", x.bandwidth())
      .attr("height", d => innerHeight - y(d.total_quantity))
      .attr("fill", "#0d6efd");

  }, [data]);

  return <svg ref={svgRef}></svg>;
}

export default D3plot
