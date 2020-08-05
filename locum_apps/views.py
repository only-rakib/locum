from django.shortcuts import render

# Create your views here.


def home_view(request):
    return render(request, 'locum_home.html')


def apply_view(request):
    profession = [
        "NP",
        "PA",
        "CRNA"
    ]
    Specialty = [
        "Physician",
        "Anesthesiology",
        "Cardiology",
        "Cardiology - Interventional",
        "Critical Care",
        "Dermatology",
        "Emergency Medicine",
        "Endocrinology",
        "Family Medicine",
        "Gastroenterology",
        "Geriatric Medicine",
        "Hematology",
        "Hospital Medicine",
        "Hospitalist - Pediatrics",
        "Internal Medicine",
        "Neurology",
        "Nephrology",
        "Oncology",
        "Ophthalmology",
        "Pathology",
        "Physical Medicine & Rehab",
        "Psychiatry",
        "Psychiatry - Child & Adolescent",
        "Pulmonology",
        "Radiology",
        "Radiology - Interventional",
        "Rheumatology",
        "Surgery - Cardiac",
        "Surgery - Colon & Rectal",
        "Surgery - General",
        "Surgery - Orthopedic",
        "Surgery - Otolaryngology (ENT)",
        "Surgery - Neuro",
        "Surgery - OB/GYN",
        "Surgery - Pediatrics",
        "Surgery - Plastic",
        "Surgery - Thoracic",
        "Surgery - Transplant",
        "Surgery - Trauma",
        "Surgery - Urology",
        "Surgery - Vascular",
        "Urgent Care",
        "Other"

    ]
    context = {'pro': profession, 'spe': Specialty}
    return render(request, 'locum_apply.html', context)


def contact_us_view(request):
    return render(request, 'locum_contact_us.html')


def job_search_view(request):
    all_location = ["California", "Louisiana",
                    "Massachusetts", "Nebraska", "New York", "Ohio"]
    return render(request, 'locum_job_search.html', {'data': all_location})


def resourse_view(request):
    data = {
        'What are locum tenens? ': '''From a latin phrase meaning “to substitute or hold the place of,” locum tenens is the industry term used to describe healthcare providers who take temporary positions at healthcare facilities. Hospitals, clinics and medical groups typically use locum tenens providers to fill vacation or maternity leaves, open positions, or part-time positions.''',
        'How long are the assignments? ': '''Assignment lengths vary. Some can be just a few days, some can be weeks, months or even a year. Some assignments are temp-to-perm. The more flexible your schedule, the more opportunity you have for placement.''',
        'Why should I consider locum tenens work? ': '''Healthcare providers report several reasons for choosing locum tenens assignments. Some do it to have greater autonomy, to earn more money or to cut back on their hours. Some like to travel and prefer to take varied assignments in different states. For some providers, locum tenens can be a way to try out a job or healthcare facility before making a full-time commitment.''',
        'How does licensure work for locum tenens providers? ': '''You will need a license to practice in any state that you ultimately work. Locums Choice will help you in obtaining licensure for different states and any other credentialing required to work in other states.''',
        'Who pays me? ': '''You are paid as an independent contractor by the locum tenens agency that places you. Your expenses, such as housing and travel are fully covered, as is your malpractice insurance.''',
        'What protections do I have as a locum tenens provider? ': '''At Locums Choice, all of our providers are covered by A++ occurrence malpractice insurance. This is forever coverage.''',
        'How often am I paid? ': '''Through Locums Choice, you will be paid bi-weekly with an option for direct deposit.''',
        'Who makes my travel and housing arrangements? ': '''Locums Choice will handle all of the logistics for your travel and housing. If you have special requirements, make sure and let us know and we’ll note your needs in your profile.''',
        'Why do I need to fill out an application? ': '''Why do I need to fill out an application? '''


    }
    return render(request, 'locum_resourse.html', {'ques': data})


def employers_view(request):
    return render(request, 'locum_employers.html')


def tenens_View(request):
    data = {
        'Superior Malpractice Coverage ': '''We offer lifetime protection through Medical Protective with limits for $1,000,000 per occurrence and $3,000,000 per annual aggregate per provider, plus defense expenses outside of these limits and zero deductible. MedPro is A++ rated by A.M. Best and licensed and admitted in all 50 states.''',
        'Concierge Travel Support ': '''Getting to your assignment should be the easy part. Working with trusted travel partners, we’ll arrange your air and ground travel and ensure that your accommodations are comfortable and ready when you arrive. If you have questions, we’re here to help. A Locums Choice advisor is available for support 24/7.''',
        'Timely Payment ': '''As an independent contractor, you should be paid fairly and promptly. All Locums Choice providers are paid on a bi-weekly schedule. For your convenience, a direct deposit option is available.''',
        'Expert Credentialing Assistance ': '''The documentation requirements for locum tenens are as rigorous as those for full-time employment. Our experienced staff is here to guide you through the credentialing process, including the new Interstate Medical Licensure Compact. We help you navigate state-specific requirements, collect documents and references, and ensure that your profile remains up to date, so you are ready for placement as opportunities arise.''',
        'Industry Experience': '''We’ve stocked Locums Choice with deeply experienced professionals from the locum tenens industry. You benefit by working with a team of knowledgeable experts who understand the nuances of locum tenens staffing and the specialized needs of providers. We love what we do, and we can’t wait to work with you.''',
        'More Jobs ': '''As a high-growth national locum tenens firms, we offer more jobs nationwide. You’ll have insider access to unadvertised opportunities, and we proactively market you before your contract ends to keep you consistently employed.'''

    }
    return render(request, 'Locum_Tenens.html', {'ques': data})


def about_View(request):
    return render(request, 'locum_aboutus.html')


def job_details_View(request):
    return render(request, 'locum_job_details.html')
