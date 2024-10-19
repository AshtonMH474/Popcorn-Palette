import logo from '../../Static/2938928.webp'

function BottomInfo(){
    return (
        <>
        <div className="lightBlack displayFlex alignBottom spaceBetween littleBottomPadding">
            <p className='leftPageBorder whiteFont smallFont noMargin'>© 2024 Popcorn Palette. All rights reserved.</p>
            <img className="smallLogo" src={logo} />
            <a className="github rightPageBorder fontLight whiteFont smallFont" href='https://github.com/AshtonMH474/Popcorn-Palette/wiki'>GitHub</a>
      </div>
        </>
    )
}

export default BottomInfo
