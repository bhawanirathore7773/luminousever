from django.db import migrations

SAP_CATEGORY = {
    "name": "SAP Consulting",
    "slug": "sap-consulting",
    "tagline": "Enterprise systems & transformation",
    "description": "Independent SAP consulting for businesses and manufacturers — from ERP strategy and implementation to migration, integration, development, analytics and application support.",
    "order": 5,
}

SAP_SERVICES = [
    {
        "order": 1,
        "name": "SAP S/4HANA Consulting & Implementation",
        "slug": "sap-s4hana-consulting",
        "short_description": "SAP S/4HANA consulting, implementation and optimisation for finance, sales, procurement, manufacturing and supply chain.",
        "hero_subtitle": "Plan, implement and improve SAP S/4HANA around the way your business actually operates — with functional, technical and project expertise.",
        "problem": "SAP transformation projects can become expensive and difficult when business processes, master data, integrations and technical changes are handled in isolation.",
        "solution": "Our SAP team combines business-process understanding with functional and technical delivery to assess your landscape, design the target process, configure the solution, coordinate testing and support go-live and optimisation.",
        "features": [
            {"title": "Business process assessment", "description": "Map current processes, pain points and requirements across finance, procurement, sales, manufacturing and supply chain."},
            {"title": "Implementation & configuration", "description": "Functional configuration, integration planning, testing and deployment support aligned to your operating model."},
            {"title": "Data & cutover planning", "description": "Plan master-data readiness, migration activities, testing cycles and go-live cutover with clear ownership."},
            {"title": "Post-go-live optimisation", "description": "Stabilise the solution, resolve issues and improve processes after go-live."},
        ],
        "technologies": ["SAP S/4HANA", "SAP Cloud ERP", "SAP Fiori", "SAP HANA", "SAP Activate", "SAP Cloud ALM"],
        "benefits": ["Clearer transformation roadmap", "Better process alignment", "Reduced implementation risk", "Stronger post-go-live adoption"],
        "who_its_for": ["Manufacturers moving to S/4HANA", "Growing businesses modernising ERP", "Companies planning SAP cloud transformation"],
        "deliverables": ["SAP landscape assessment", "Process and solution blueprint", "Configuration and development plan", "Testing and cutover support", "Go-live and hypercare support"],
        "faqs": [
            {"question": "Can you help with a new SAP implementation?", "answer": "Yes. We can support discovery, process design, functional work, technical development, integrations, testing, cutover and post-go-live support based on your project scope."},
            {"question": "Do you support manufacturing businesses?", "answer": "Yes. Our SAP offering covers manufacturing-focused processes including production, procurement, inventory, sales, quality and maintenance."},
        ],
        "meta_title": "SAP S/4HANA Consulting & Implementation | Luminous Ever",
        "meta_description": "SAP S/4HANA consulting and implementation for businesses and manufacturers. Functional, technical, integration, testing and post-go-live SAP support.",
    },
    {
        "order": 2,
        "name": "SAP ECC to S/4HANA Migration",
        "slug": "sap-ecc-to-s4hana-migration",
        "short_description": "Plan and execute SAP ECC to S/4HANA migration with process, data, custom-code and integration readiness.",
        "hero_subtitle": "Move from SAP ECC to S/4HANA with a practical migration roadmap covering business processes, data, custom developments, integrations and testing.",
        "problem": "ECC-to-S/4HANA transformation involves more than a technical upgrade. Custom code, data quality, interfaces, business processes and user adoption can all affect the outcome.",
        "solution": "We assess the existing SAP landscape, identify migration dependencies, plan the target architecture and coordinate functional and technical workstreams through testing and go-live.",
        "features": [
            {"title": "Readiness assessment", "description": "Review the current ECC landscape, business processes, custom developments, interfaces and data dependencies."},
            {"title": "Migration roadmap", "description": "Define scope, approach, workstreams, milestones, testing strategy and cutover planning."},
            {"title": "Custom code & integration readiness", "description": "Identify enhancement, interface and integration impacts that need remediation or redesign."},
            {"title": "Testing & cutover support", "description": "Support functional testing, defect resolution, cutover preparation and hypercare."},
        ],
        "technologies": ["SAP ECC", "SAP S/4HANA", "SAP HANA", "SAP Fiori", "SAP Integration Suite", "SAP Cloud ALM"],
        "benefits": ["Lower migration uncertainty", "Better technical readiness", "Controlled cutover", "Modern ERP foundation"],
        "who_its_for": ["ECC customers planning S/4HANA", "Manufacturers preparing ERP transformation", "Businesses evaluating SAP cloud migration"],
        "deliverables": ["Landscape assessment", "Migration roadmap", "Custom-code and integration assessment", "Testing plan", "Cutover and hypercare support"],
        "faqs": [
            {"question": "Can you assess our existing ECC system first?", "answer": "Yes. An assessment is the best starting point to understand custom code, interfaces, data, business processes and migration risks before selecting the migration approach."},
        ],
        "meta_title": "SAP ECC to S/4HANA Migration Consulting",
        "meta_description": "SAP ECC to S/4HANA migration consulting covering readiness, data, custom code, integrations, testing, cutover and post-go-live support.",
    },
    {
        "order": 3,
        "name": "SAP FI/CO Consulting",
        "slug": "sap-fi-co-consulting",
        "short_description": "SAP Finance and Controlling consulting for accounting, reporting, costing, profitability and management control.",
        "hero_subtitle": "Strengthen finance processes with SAP FI/CO expertise across accounting, controlling, reporting, costing and business integration.",
        "problem": "Finance teams often struggle when SAP configuration, reporting, master data and operational processes do not align with management requirements.",
        "solution": "We help design and optimise finance processes across FI and CO, connect finance with operational modules and improve reporting and controls.",
        "features": [
            {"title": "Financial accounting", "description": "Support core finance processes including general ledger, accounts payable, accounts receivable and asset accounting."},
            {"title": "Controlling", "description": "Support cost centres, internal orders, profitability analysis and management reporting."},
            {"title": "Integration with operations", "description": "Align finance with procurement, sales, inventory, production and other business processes."},
            {"title": "Reporting & optimisation", "description": "Improve reporting structures, controls and process efficiency."},
        ],
        "technologies": ["SAP FI", "SAP CO", "SAP S/4HANA Finance", "SAP Fiori", "SAP Analytics Cloud"],
        "benefits": ["Stronger financial controls", "Better management visibility", "Cleaner process integration", "Improved reporting"],
        "who_its_for": ["Manufacturers", "Mid-market and enterprise businesses", "Finance teams modernising SAP"],
        "deliverables": ["Process assessment", "Functional configuration support", "Reporting requirements", "Testing support", "Post-go-live optimisation"],
        "faqs": [
            {"question": "Can FI/CO integrate with manufacturing and procurement?", "answer": "Yes. SAP Finance and Controlling are designed to connect with operational processes, and we can help align those integrations to your requirements."},
        ],
        "meta_title": "SAP FI CO Consulting Services | Finance & Controlling",
        "meta_description": "SAP FI/CO consulting for finance, accounting, controlling, costing, reporting and integrated business processes.",
    },
    {
        "order": 4,
        "name": "SAP MM & Procurement Consulting",
        "slug": "sap-mm-procurement",
        "short_description": "SAP Materials Management and procurement consulting for purchasing, inventory, material master and procure-to-pay.",
        "hero_subtitle": "Improve purchasing, inventory and procure-to-pay processes with SAP MM consulting built around operational control and visibility.",
        "problem": "Poor material data, disconnected purchasing processes and weak inventory controls can create delays, excess stock and avoidable procurement costs.",
        "solution": "We optimise SAP MM processes across material master, purchasing, inventory management, valuation and integration with finance, production and sales.",
        "features": [
            {"title": "Procure-to-pay", "description": "Improve requisition, purchase order, goods receipt and invoice processes."},
            {"title": "Material master & inventory", "description": "Improve material data structures, inventory visibility and stock movement processes."},
            {"title": "Vendor and purchasing processes", "description": "Align purchasing workflows, approvals and vendor-related processes."},
            {"title": "Integration", "description": "Connect procurement with FI/CO, PP, SD, warehouse and external systems."},
        ],
        "technologies": ["SAP MM", "SAP S/4HANA Procurement", "SAP Fiori", "SAP Ariba", "SAP Integration Suite"],
        "benefits": ["Better procurement visibility", "Improved inventory control", "Faster purchasing cycles", "Cleaner master data"],
        "who_its_for": ["Manufacturers", "Wholesale and distribution businesses", "Procurement teams using SAP"],
        "deliverables": ["Procurement process assessment", "Configuration support", "Master-data guidance", "Integration and testing support"],
        "faqs": [
            {"question": "Can you support SAP MM for manufacturing?", "answer": "Yes. We can align purchasing, inventory and material processes with production, finance and warehouse requirements."},
        ],
        "meta_title": "SAP MM Consulting & Procurement Services",
        "meta_description": "SAP MM consulting for procurement, purchasing, inventory, material master, procure-to-pay and SAP integration.",
    },
    {
        "order": 5,
        "name": "SAP SD & Order-to-Cash Consulting",
        "slug": "sap-sd-order-to-cash",
        "short_description": "SAP Sales and Distribution consulting for quotations, orders, pricing, delivery, billing and order-to-cash.",
        "hero_subtitle": "Streamline sales, pricing, delivery and billing with SAP SD consulting that connects customer demand to fulfilment and finance.",
        "problem": "Sales processes become difficult to control when pricing, orders, inventory, delivery, billing and finance are not connected cleanly.",
        "solution": "We improve SAP SD processes across sales orders, pricing, availability, delivery, billing and integration with finance and inventory.",
        "features": [
            {"title": "Sales order management", "description": "Support quotation, order, availability and fulfilment processes."},
            {"title": "Pricing & billing", "description": "Review pricing conditions, billing flows and finance integration."},
            {"title": "Delivery & fulfilment", "description": "Improve delivery processes and integration with inventory and logistics."},
            {"title": "Order-to-cash optimisation", "description": "Map the complete customer order lifecycle and remove process bottlenecks."},
        ],
        "technologies": ["SAP SD", "SAP S/4HANA Sales", "SAP Fiori", "SAP EWM", "SAP FI"],
        "benefits": ["Faster order processing", "Better fulfilment visibility", "Improved billing accuracy", "Stronger finance integration"],
        "who_its_for": ["Manufacturers", "Distributors", "B2B sales organisations", "Businesses with complex order flows"],
        "deliverables": ["O2C process assessment", "Functional configuration support", "Pricing and billing review", "Testing and optimisation"],
        "faqs": [
            {"question": "Can SAP SD connect with warehouse and finance processes?", "answer": "Yes. SAP SD commonly integrates with inventory, warehouse and finance processes, and we can help design the required end-to-end flow."},
        ],
        "meta_title": "SAP SD Consulting | Sales & Order-to-Cash",
        "meta_description": "SAP SD consulting for sales, pricing, order management, delivery, billing and end-to-end order-to-cash processes.",
    },
    {
        "order": 6,
        "name": "SAP PP & Manufacturing Consulting",
        "slug": "sap-pp-manufacturing",
        "short_description": "SAP Production Planning consulting for MRP, BOMs, routings, production orders and manufacturing execution.",
        "hero_subtitle": "Connect planning and production with SAP PP expertise for MRP, BOMs, routings, production orders and manufacturing operations.",
        "problem": "Manufacturers lose efficiency when production planning, material availability, shop-floor execution and inventory are disconnected.",
        "solution": "We help manufacturers optimise SAP PP processes and integrate production planning with MM, SD, QM, PM and finance.",
        "features": [
            {"title": "MRP & planning", "description": "Support material requirements planning, demand-driven planning and exception handling."},
            {"title": "BOM & routing", "description": "Improve product structures, work centres, routings and production master data."},
            {"title": "Production orders", "description": "Support order creation, release, confirmation, goods movement and settlement processes."},
            {"title": "Manufacturing integration", "description": "Connect PP with procurement, quality, maintenance, sales and inventory."},
        ],
        "technologies": ["SAP PP", "SAP S/4HANA Manufacturing", "SAP MRP", "SAP Fiori", "SAP Digital Manufacturing"],
        "benefits": ["Better production visibility", "Improved planning", "Fewer material shortages", "Stronger plant integration"],
        "who_its_for": ["Discrete manufacturers", "Process manufacturers", "Engineering and industrial businesses"],
        "deliverables": ["Manufacturing process assessment", "PP configuration support", "Master-data review", "Testing and go-live support"],
        "faqs": [
            {"question": "Do you support SAP PP for manufacturing plants?", "answer": "Yes. We focus on production planning and its integration with procurement, inventory, quality, maintenance and sales."},
        ],
        "meta_title": "SAP PP Consulting | Production Planning & Manufacturing",
        "meta_description": "SAP PP consulting for production planning, MRP, BOMs, routings, production orders and manufacturing integration.",
    },
    {
        "order": 7,
        "name": "SAP PM & QM Consulting",
        "slug": "sap-pm-qm-consulting",
        "short_description": "SAP Plant Maintenance and Quality Management consulting for asset reliability, inspections and quality processes.",
        "hero_subtitle": "Improve asset reliability and product quality with SAP PM and QM processes integrated into your manufacturing operation.",
        "problem": "Unplanned downtime, weak maintenance history and inconsistent quality processes can affect production, delivery and customer confidence.",
        "solution": "We help configure and optimise maintenance and quality workflows, integrating them with production, inventory and finance.",
        "features": [
            {"title": "Plant maintenance", "description": "Support equipment master data, notifications, maintenance orders and preventive maintenance."},
            {"title": "Quality management", "description": "Support inspections, quality notifications, results recording and quality decisions."},
            {"title": "Operational integration", "description": "Connect PM and QM with production, inventory, procurement and finance."},
            {"title": "Reporting & controls", "description": "Improve visibility into asset performance, maintenance and quality trends."},
        ],
        "technologies": ["SAP PM", "SAP QM", "SAP S/4HANA Asset Management", "SAP Fiori"],
        "benefits": ["Improved asset visibility", "Better preventive maintenance", "Stronger quality controls", "Reduced process fragmentation"],
        "who_its_for": ["Manufacturing plants", "Asset-intensive businesses", "Industrial operations"],
        "deliverables": ["PM/QM process assessment", "Configuration support", "Master-data review", "Testing and optimisation"],
        "faqs": [
            {"question": "Can PM and QM integrate with production?", "answer": "Yes. We can design end-to-end processes that connect maintenance and quality activities with production and inventory."},
        ],
        "meta_title": "SAP PM QM Consulting | Maintenance & Quality",
        "meta_description": "SAP PM and QM consulting for plant maintenance, asset management, inspections, quality processes and manufacturing integration.",
    },
    {
        "order": 8,
        "name": "SAP ABAP, Fiori & Custom Development",
        "slug": "sap-abap-fiori-development",
        "short_description": "SAP ABAP, CDS, OData, Fiori and custom enhancement services for business-specific requirements.",
        "hero_subtitle": "Extend SAP safely with experienced ABAP and Fiori development for reports, interfaces, workflows, enhancements and business applications.",
        "problem": "Standard SAP functionality cannot always cover unique business requirements, but unmanaged customisation can create long-term technical debt.",
        "solution": "We design maintainable SAP extensions using appropriate ABAP and Fiori technologies, with attention to clean-core principles, testing and upgrade readiness.",
        "features": [
            {"title": "ABAP development", "description": "Reports, enhancements, forms, interfaces, BAdIs, user exits and custom programs."},
            {"title": "Fiori & UI development", "description": "Modern SAP user experiences using Fiori, OData and related services."},
            {"title": "Interfaces & APIs", "description": "Develop and maintain SAP integrations using APIs, IDocs, OData and integration platforms."},
            {"title": "Custom enhancements", "description": "Extend standard processes while considering maintainability and upgrade impact."},
        ],
        "technologies": ["ABAP", "ABAP OO", "CDS Views", "OData", "SAP Fiori", "SAP UI5", "APIs", "IDoc"],
        "benefits": ["Business-specific functionality", "Modern user experience", "Maintainable custom development", "Better integration capability"],
        "who_its_for": ["SAP customers with custom requirements", "Manufacturers needing tailored workflows", "Teams maintaining legacy ABAP applications"],
        "deliverables": ["Technical assessment", "Development specification", "ABAP/Fiori development", "Testing and deployment support"],
        "faqs": [
            {"question": "Can you handle existing ABAP programs?", "answer": "Yes. We can review, debug, enhance and modernise existing custom developments as part of an SAP technical support engagement."},
        ],
        "meta_title": "SAP ABAP & Fiori Development Services",
        "meta_description": "SAP ABAP, Fiori, UI5, CDS, OData, IDoc, reports, enhancements, interfaces and custom SAP development services.",
    },
    {
        "order": 9,
        "name": "SAP BTP & Integration Services",
        "slug": "sap-btp-integration",
        "short_description": "SAP BTP, Integration Suite, APIs and enterprise integration for SAP and non-SAP systems.",
        "hero_subtitle": "Connect SAP and non-SAP applications with SAP BTP and Integration Suite for secure, scalable business processes.",
        "problem": "Disconnected ERP, CRM, e-commerce, warehouse and third-party applications create duplicate data, manual work and fragile interfaces.",
        "solution": "We design integration architectures and implement APIs, interfaces, events and workflows using SAP BTP and Integration Suite where appropriate.",
        "features": [
            {"title": "SAP Integration Suite", "description": "Design and support application-to-application integrations across SAP and third-party systems."},
            {"title": "API integration", "description": "Build secure, reusable APIs and integration flows around business processes."},
            {"title": "SAP BTP extensions", "description": "Extend SAP applications while keeping core processes maintainable and upgrade-ready."},
            {"title": "Migration & modernisation", "description": "Support migration from legacy integration approaches toward modern SAP integration patterns."},
        ],
        "technologies": ["SAP BTP", "SAP Integration Suite", "API Management", "Cloud Integration", "Event Mesh", "SAP Build"],
        "benefits": ["Connected enterprise systems", "Reduced manual data entry", "Reusable integrations", "More scalable architecture"],
        "who_its_for": ["Businesses with SAP and third-party systems", "Manufacturers with complex plant integrations", "Companies modernising legacy interfaces"],
        "deliverables": ["Integration assessment", "Architecture design", "Integration flows/APIs", "Monitoring and support", "Migration roadmap"],
        "faqs": [
            {"question": "Can you integrate SAP with non-SAP applications?", "answer": "Yes. SAP BTP and Integration Suite can support integration across SAP and third-party applications, depending on the systems and interface requirements."},
        ],
        "meta_title": "SAP BTP & Integration Suite Consulting",
        "meta_description": "SAP BTP and Integration Suite consulting for APIs, Cloud Integration, enterprise integration, extensions and SAP/non-SAP connectivity.",
    },
    {
        "order": 10,
        "name": "SAP Analytics Cloud & Business Reporting",
        "slug": "sap-analytics-cloud",
        "short_description": "SAP Analytics Cloud, reporting and planning solutions for finance, operations, sales and management.",
        "hero_subtitle": "Turn SAP data into useful management insight with SAP Analytics Cloud, reporting, planning and decision-support solutions.",
        "problem": "Businesses often have valuable SAP data but struggle to turn it into timely, trusted dashboards and planning views.",
        "solution": "We help connect business data, define reporting requirements and build dashboards and planning experiences that support practical decisions.",
        "features": [
            {"title": "Management dashboards", "description": "Build role-based dashboards for finance, sales, procurement, operations and management."},
            {"title": "Planning & forecasting", "description": "Support planning models and scenario analysis around business drivers."},
            {"title": "SAP data connectivity", "description": "Connect analytics with SAP S/4HANA and relevant data sources."},
            {"title": "KPI design", "description": "Translate business questions into clear KPIs and decision-oriented reporting."},
        ],
        "technologies": ["SAP Analytics Cloud", "SAP S/4HANA", "SAP Datasphere", "SAP Business Data Cloud"],
        "benefits": ["Faster decision-making", "Trusted management reporting", "Better planning visibility", "Role-based insights"],
        "who_its_for": ["CFO and finance teams", "Manufacturing leadership", "Sales and supply chain teams", "Businesses modernising reporting"],
        "deliverables": ["Analytics assessment", "Dashboard design", "KPI framework", "Planning/reporting implementation", "User enablement"],
        "faqs": [
            {"question": "Can SAP Analytics Cloud connect to S/4HANA?", "answer": "Yes. SAP Analytics Cloud can connect with SAP data sources including SAP S/4HANA, with the architecture depending on the reporting and planning requirements."},
        ],
        "meta_title": "SAP Analytics Cloud Consulting & Reporting",
        "meta_description": "SAP Analytics Cloud consulting for dashboards, planning, forecasting, KPIs and management reporting across SAP data.",
    },
    {
        "order": 11,
        "name": "SAP EWM & Transportation Management",
        "slug": "sap-ewm-tm",
        "short_description": "SAP Extended Warehouse Management and Transportation Management for logistics and supply chain execution.",
        "hero_subtitle": "Improve warehouse and transportation execution with SAP EWM and TM consulting connected to your end-to-end supply chain.",
        "problem": "Complex warehouse and transportation operations need accurate inventory, efficient movement and reliable delivery planning.",
        "solution": "We help align warehouse and transportation processes with procurement, production, sales and supply chain requirements.",
        "features": [
            {"title": "Warehouse processes", "description": "Support inbound, outbound, storage, picking, packing and inventory movement processes."},
            {"title": "Transportation planning", "description": "Support transportation planning and execution across relevant logistics flows."},
            {"title": "End-to-end integration", "description": "Connect warehouse and transport execution with S/4HANA business processes."},
            {"title": "Operational visibility", "description": "Improve process monitoring and exception handling."},
        ],
        "technologies": ["SAP EWM", "SAP TM", "SAP S/4HANA", "SAP Fiori"],
        "benefits": ["Better warehouse visibility", "Improved logistics execution", "Fewer manual handoffs", "Stronger supply chain control"],
        "who_its_for": ["Manufacturers", "Distributors", "Warehouses and logistics operations"],
        "deliverables": ["Logistics process assessment", "Functional consulting", "Integration support", "Testing and optimisation"],
        "faqs": [
            {"question": "Can EWM and TM be integrated with S/4HANA?", "answer": "Yes. We can assess the required architecture and end-to-end integration based on your deployment and logistics processes."},
        ],
        "meta_title": "SAP EWM & TM Consulting | Warehouse & Transport",
        "meta_description": "SAP EWM and TM consulting for warehouse management, transportation, logistics execution and S/4HANA integration.",
    },
    {
        "order": 12,
        "name": "SAP SuccessFactors & HCM Consulting",
        "slug": "sap-successfactors-hcm",
        "short_description": "SAP SuccessFactors and HCM consulting for core HR, employee processes, talent and workforce transformation.",
        "hero_subtitle": "Modernise HR processes with SAP SuccessFactors consulting aligned to your people, policies and business operations.",
        "problem": "HR teams need consistent employee data, efficient processes and connected workforce experiences across the employee lifecycle.",
        "solution": "We support SAP SuccessFactors and HCM transformation with process assessment, configuration, integration and adoption support.",
        "features": [
            {"title": "Core HR", "description": "Support employee data and core HR process design."},
            {"title": "Talent processes", "description": "Support recruiting, onboarding, performance and employee experience scenarios."},
            {"title": "Integration", "description": "Connect HR processes with relevant enterprise systems and data flows."},
            {"title": "Adoption & support", "description": "Help teams transition to new processes and stabilise the solution."},
        ],
        "technologies": ["SAP SuccessFactors", "SAP HCM", "SAP Integration Suite", "SAP BTP"],
        "benefits": ["More consistent HR processes", "Better employee data", "Improved workforce visibility", "Connected enterprise HR"],
        "who_its_for": ["Growing organisations", "Manufacturers with large workforces", "Businesses modernising HR systems"],
        "deliverables": ["HR process assessment", "Solution configuration support", "Integration planning", "Testing and adoption support"],
        "faqs": [
            {"question": "Do you support SAP SuccessFactors integrations?", "answer": "Yes. We can assess HR integration requirements and help connect SuccessFactors with relevant enterprise applications."},
        ],
        "meta_title": "SAP SuccessFactors & HCM Consulting",
        "meta_description": "SAP SuccessFactors and HCM consulting for core HR, talent, employee processes, integration and workforce transformation.",
    },
    {
        "order": 13,
        "name": "SAP Ariba, Concur & Spend Management",
        "slug": "sap-ariba-concur",
        "short_description": "SAP spend-management consulting for procurement, sourcing, travel, expense and supplier processes.",
        "hero_subtitle": "Connect procurement, supplier, travel and expense processes with SAP spend-management solutions and your ERP landscape.",
        "problem": "Spend processes can become fragmented across procurement, suppliers, employee expenses and ERP systems, reducing visibility and control.",
        "solution": "We help assess and integrate SAP spend-management processes with core SAP business operations, focusing on practical adoption and clean data flows.",
        "features": [
            {"title": "SAP Ariba", "description": "Support procurement and supplier-related process transformation."},
            {"title": "SAP Concur", "description": "Support travel and expense process improvement and integration."},
            {"title": "ERP integration", "description": "Connect spend processes with SAP finance and procurement workflows."},
            {"title": "Process optimisation", "description": "Improve controls, approvals, visibility and user experience."},
        ],
        "technologies": ["SAP Ariba", "SAP Concur", "SAP S/4HANA", "SAP Integration Suite"],
        "benefits": ["Better spend visibility", "Stronger procurement controls", "Reduced manual work", "Connected finance processes"],
        "who_its_for": ["Procurement organisations", "Manufacturers and enterprises", "Businesses modernising spend management"],
        "deliverables": ["Process assessment", "Integration planning", "Configuration support", "Testing and adoption support"],
        "faqs": [
            {"question": "Can SAP Ariba connect with S/4HANA?", "answer": "Yes. Integration requirements depend on the selected Ariba processes, S/4HANA setup and business landscape."},
        ],
        "meta_title": "SAP Ariba & Concur Consulting Services",
        "meta_description": "SAP Ariba, Concur and spend-management consulting for procurement, sourcing, travel, expense and ERP integration.",
    },
    {
        "order": 14,
        "name": "SAP AMS & Application Support",
        "slug": "sap-ams-support",
        "short_description": "Ongoing SAP application management, incident support, enhancements, monitoring and optimisation.",
        "hero_subtitle": "Keep your SAP landscape stable and improving with experienced application support, troubleshooting and continuous optimisation.",
        "problem": "After go-live, SAP systems still need incident resolution, monitoring, enhancements, testing and process optimisation — and internal teams may not have capacity for everything.",
        "solution": "We provide flexible SAP application support across functional and technical areas, with structured issue handling and continuous improvement.",
        "features": [
            {"title": "Functional support", "description": "Troubleshoot business-process issues across supported SAP modules."},
            {"title": "Technical support", "description": "Support ABAP, interfaces, jobs, reports, authorisations and technical issues within scope."},
            {"title": "Enhancements & change requests", "description": "Handle small improvements and controlled enhancements as business needs evolve."},
            {"title": "Monitoring & optimisation", "description": "Identify recurring issues, performance concerns and opportunities for process improvement."},
        ],
        "technologies": ["SAP S/4HANA", "SAP ECC", "ABAP", "Fiori", "SAP BTP", "SAP Integration Suite"],
        "benefits": ["Faster issue resolution", "Predictable support coverage", "Continuous improvement", "Reduced internal support burden"],
        "who_its_for": ["Businesses already running SAP", "Manufacturers with lean IT teams", "Companies needing post-go-live support"],
        "deliverables": ["Support model", "Incident and change handling", "Enhancement support", "Root-cause analysis", "Continuous improvement reviews"],
        "faqs": [
            {"question": "Can you support an SAP system you did not implement?", "answer": "Yes. We can start with a technical and functional discovery so the team understands your landscape, processes and support priorities."},
            {"question": "Do you offer ongoing SAP support?", "answer": "Yes. Support can be structured around the SAP modules, technical areas and response model your business needs."},
        ],
        "meta_title": "SAP AMS & Application Support Services",
        "meta_description": "SAP AMS and application support for S/4HANA, ECC, ABAP, Fiori, integrations, incidents, enhancements and optimisation.",
    },
]

def seed(apps, schema_editor):
    ServiceCategory = apps.get_model("services", "ServiceCategory")
    Service = apps.get_model("services", "Service")
    Industry = apps.get_model("services", "Industry")

    category, _ = ServiceCategory.objects.get_or_create(slug=SAP_CATEGORY["slug"], defaults=SAP_CATEGORY)

    for item in SAP_SERVICES:
        data = dict(item)
        data["category_id"] = category.id
        Service.objects.update_or_create(slug=data["slug"], defaults=data)

    manufacturing, _ = Industry.objects.get_or_create(
        slug="manufacturing",
        defaults={
            "name": "Manufacturing",
            "description": "Manufacturing businesses need connected processes across procurement, production, inventory, quality, maintenance, sales, finance and supply chain. We combine digital growth services with SAP consulting to help manufacturers improve both customer-facing visibility and enterprise operations.",
            "challenges": [
                "Connecting procurement, production, inventory and finance processes",
                "Modernising SAP ECC landscapes and planning S/4HANA transformation",
                "Improving production planning, quality and plant maintenance visibility",
                "Generating qualified B2B enquiries through search and digital channels",
            ],
            "meta_title": "Manufacturing Digital & SAP Consulting Services",
            "meta_description": "Digital marketing, websites and SAP consulting for manufacturers — S/4HANA, PP, MM, SD, FI/CO, PM/QM, ABAP, BTP and support.",
            "is_published": True,
            "order": 3,
        },
    )
    manufacturing.description = "Manufacturing businesses need connected processes across procurement, production, inventory, quality, maintenance, sales, finance and supply chain. We combine digital growth services with SAP consulting to help manufacturers improve both customer-facing visibility and enterprise operations."
    manufacturing.challenges = [
        "Connecting procurement, production, inventory and finance processes",
        "Modernising SAP ECC landscapes and planning S/4HANA transformation",
        "Improving production planning, quality and plant maintenance visibility",
        "Generating qualified B2B enquiries through search and digital channels",
    ]
    manufacturing.meta_title = "Manufacturing Digital & SAP Consulting Services"
    manufacturing.meta_description = "Digital marketing, websites and SAP consulting for manufacturers — S/4HANA, PP, MM, SD, FI/CO, PM/QM, ABAP, BTP and support."
    manufacturing.save()
    manufacturing.relevant_services.add(*Service.objects.filter(slug__in=[s["slug"] for s in SAP_SERVICES]))

def unseed(apps, schema_editor):
    ServiceCategory = apps.get_model("services", "ServiceCategory")
    Service = apps.get_model("services", "Service")
    Service.objects.filter(slug__in=[s["slug"] for s in SAP_SERVICES]).delete()
    ServiceCategory.objects.filter(slug=SAP_CATEGORY["slug"]).delete()

class Migration(migrations.Migration):
    dependencies = [
        ("services", "0002_seed_services_and_industries"),
    ]
    operations = [
        migrations.RunPython(seed, unseed),
    ]
