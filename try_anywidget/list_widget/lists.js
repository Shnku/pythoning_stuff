function render({ model, el }) {
    // Container for all elements
    const container = document.createElement("div");
    container.style.padding = "10px";
    container.style.border = "1px solid #ccc";

    // Function to render nodes
    const renderNodes = (names) => {
        container.innerHTML = ""; // clear previous content
        names.forEach((name, i) => {
            const div = document.createElement("div");
            div.textContent = `Node ${i + 1}: ${name}`;
            div.style.margin = "4px";
            div.style.padding = "4px";
            div.style.background = "#0030f0";
            container.appendChild(div);
        });
    };

    // Initial render
    renderNodes(model.get("names"));

    // Re-render when names change
    model.on("change:names", () => renderNodes(model.get("names")));

    el.appendChild(container);
}    export default { render };
